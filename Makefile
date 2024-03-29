PELICAN=pelican
BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py


html:
	source venv/bin/activate ; python create_pages.py
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)"

html-publish:
	source venv/bin/activate ; python create_pages.py
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)"

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)"

compile-lco-intro:
	cd lco-intro-twinery ; $(MAKE) compile

rsync_upload: html-publish compile-lco-intro
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --include tags --cvs-exclude --delete "$(OUTPUTDIR)"/ "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)/blog"
	scp -P 9834 lco-intro-twinery/output.html "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)/intro/index.html"


u: upload
upload: clean html-publish rsync_upload


.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload u upload
