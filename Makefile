.PHONY : addons

addons: coop.db
	xmi2oerp -r --dbfile $< --logfile $?.log --loglevel=2 --target $@

coop.db: design/coop.uml
	xmi2oerp --infile $< --dbfile $@

