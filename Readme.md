Introduction
============
A modern Periodic Table, with latest update from [IUPAC](https://iupac.org/).

It also contains utilities such as [Vegards's Law](http://journals.aps.org/pra/abstract/10.1103/PhysRevA.43.3161).
Many other utilities are on its way.

- [Introduction](#introduction)
- [Install](#install)
  - [Dependencies](#dependencies)
    - [Linux](#linux)
    - [Mac OS X](mac)
- [Usage](#usage)
  - [Elements](#elems)
  - [Vegards Law](#vegard)
  - [Plots](#plot)
- [Contact](#contact)
- [Coffee and Cookies](#donate)
- [My Other Apps](#apps)


Install
=======
Do it in standard Linux way:

```bash 
autogen.sh; make; sudo make install
```

Dependencies
------------
This code is build using `python-3` and `Gtk-3`. So, you must have these two installed in your
system. The python modules needed are few, and mostly comes bundled with standard `python-3`
installation; or you can install them (e.g.([numpy](https://pypi.python.org/pypi/numpy),
[matplotlib](https://pypi.python.org/pypi/matplotlib/2.0.0rc1))) using `$sudo pip install <module>`.

### Linux

This application is build and tested in Gnu-Linux OS ([Fedora](https://getfedora.org/)); but, there
is no Fedora or Linux specific libraries are used. So, It should be installed natively on any
Gnu-Linux OS, supporting GTK-3 UX. If there is any problem, [contact](#contact) me.

### Mac OS X

I have not tested it for [Mac](http://www.apple.com/macos/sierra/). But, mostly, you need GTK+
obtained and build(see, [this](https://www.gtk.org/download/macos.php)).

Usage
=====

This Periodic Table can be used in multiple way.

Elements
---------
Properties of all the elements can be viewed simply by clicking into its name.

Vegards Law
-----------
Click on `utilities -> Vegards Law` to open up an window to put a binary alloy, as A50B50. It
should work on ternary alloys too, but not tested. It also shows the variation of lattice
parameters with fixed volume, helping the lattice parameter optimization.

Plots
-----
Click on `Utility->Plot-><choose>` to plot standard atomic functionals like `Atomic Radius`, `Van
der Waals Radius` etc.

Contact
=======
The preferred way of contacting me is via [github project page](https://github.com/rudrab/PeriodicTable/issues)

Coffee and Cookies
==================
If you <em>really</em> like _Periodic Table_ and found it usefull, please buy me a coffee using [PayPal](https://www.paypal.me/RudraBanerjee).


My Other Apps
=============
See other apps I have developed:

- [MkBiB](http://rudrab.github.io/MkBiB/): BiBTeX Manager

- [Periodic Table](http://rudrab.github.io/PeriodicTable/): Periodic Table and Extra

- [Shadow](http://rudrab.github.io/Shadow/): Icon theme for Gnome desktop

- [vimf90](http://rudrab.github.io/vimf90/): Change vim to a fortran IDE
