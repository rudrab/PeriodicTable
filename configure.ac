AC_PREREQ(2.52)
#m4_include([aclocal/ax_prog_perl_modules.m4])
#m4_include([aclocal/ax_python_module.m4])
AC_INIT([ptbl], [1.3],[],[ptbl])
AC_DEFINE([PACKAGE], [ptbl], [Periodic Table])
AM_INIT_AUTOMAKE([1.9.6 dist-bzip2 subdir-objects foreign])
GLIB_GSETTINGS
AM_PATH_GTK_3_0([3.4.0],,AC_MSG_ERROR([Gtk+ 3.0.0 or higher required.]))
AM_PATH_PYTHON([3.0])

AC_CONFIG_FILES([Makefile
                 ptbl/__init__.py
                 data/Makefile
                 data/ptbl.desktop
                 data/icons/Makefile
                 data/icons/hicolor/Makefile
                 data/icons/hicolor/48x48/Makefile
                 data/icons/hicolor/48x48/apps/Makefile
                 data/icons/hicolor/scalable/Makefile
                 data/icons/hicolor/scalable/apps/Makefile
                 data/ui/Makefile
                 ])
AC_OUTPUT
