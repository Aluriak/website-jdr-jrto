
backup:
	rsync --archive --delete --compress --progress --partial --human-readable root-skadi:/var/www/jdr-wiki/wiki/data/ data
	git add data
	git commit -m "backup"
