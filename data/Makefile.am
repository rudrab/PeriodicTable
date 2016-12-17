SUBDIRS = icons ui 

desktopdir = $(datadir)/applications
desktop_DATA = ptbl.desktop
gsettings_SCHEMAS = org.example.ptbl.gschema.xml
@GSETTINGS_RULES@

UPDATE_DESKTOP = update-desktop-database $(datadir)/applications || :


install-data-hook: 
	$(UPDATE_DESKTOP)
uninstall-hook: 
	$(UPDATE_DESKTOP)
	
