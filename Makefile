UML=design/coop.uml

notify:
	while inotifywait -e close_write $(UML); do make addons; done

addons: coop.db
	xmi2oerp -r --dbfile $< --logfile $?.log --loglevel=2 --target $@

coop.db: design/coop.uml
	xmi2oerp --infile $< --dbfile $@

.PHONY : notify addons

