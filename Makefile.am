ACLOCAL_AMFLAGS = -I m4


ptbldir = $(pythondir)/ptbl/
ptbl_PYTHON = $(wildcard ptbl/*.py)
bin_SCRIPTS = bin/ptbl

elemdir = $(datadir)/@PACKAGE@/
elem_DATA = ptbl/elems.db

bin/ptbl: bin/ptbl.in
	@$(MKDIR_P) bin
	$(AM_V_GEN)sed                              \
		-e s!\@prefix\@!$(prefix)!          \
		-e s!\@datadir\@!$(datadir)!        \
		-e s!\@pkgdatadir\@!$(pkgdatadir)!  \
		-e s!\@pkglibdir\@!$(pkglibdir)!    \
		-e s!\@localedir\@!$(localedir)!    \
		-e s!\@pythondir\@!$(pythondir)!    \
		-e s!\@pyexecdir\@!$(pyexecdir)!    \
		-e s!\@VERSION\@!$(VERSION)!        \
		< $< > $@
	@chmod a+x $@

run: $(BUILT_SOURCES)  bin/ptbl
	env GSETTINGS_SCHEMA_DIR=$(srcdir)/data $(srcdir)/bin/ptbl -v
data/gschemas.compiled: $(gsettings_SCHEMAS)
	$(AM_V_GEN) $(GLIB_COMPILE_SCHEMAS) data

EXTRA_DIST = $(gsettings_SCHEMAS)
CLEANFILES = data/gschemas.compiled bin/ptbl
SUBDIRS=data
dist-hook:
	@if test -d "$(srcdir)/.git"; \
	then \
		echo Creating ChangeLog && \
		( cd "$(top_srcdir)" && \
		echo '# Generated by Makefile. Do not edit.'; echo; \
		$(top_srcdir)/missing --run git log --pretty=format:"%h - %an, %ar : %s") > ChangeLog.tmp \
		&& mv -f ChangeLog.tmp $(distdir)/ChangeLog \
		|| ( rm -f ChangeLog.tmp ; \
		echo Failed to generate ChangeLog >&2 ); \
		else \
		echo A git clone is required to generate a ChangeLog >&2; \
	fi

