THEME_DEST_DIR=/var/www/jdr/wiki/lib/tpl



backup-data:
	rsync --archive --delete --compress --progress --partial --human-readable root-skadi:/var/www/jdr/wiki/data/ data
	git add data
	git commit -m "backup"



get-theme:
	rsync --archive --delete --compress --progress --partial lucas-skadi:$(THEME_DEST_DIR)/ad-hominem theme/

upload-theme:
	rsync --archive --delete --compress --progress --partial theme/ad-hominem root-skadi:$(THEME_DEST_DIR)


open-classes:
	vimoku "règles:classe:artificier" "règles:classe:maître d'armes" "règles:classe:gardien" "règles:classe:tireur d'élite" "règles:classe:antimagus" "règles:classe:officier" "règles:classe:berserk" "règles:classe:magicien" "règles:aptitude:exploration" "règles:classe:fauconnier"
