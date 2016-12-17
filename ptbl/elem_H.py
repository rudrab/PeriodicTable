#!/usr/bin/env python3
import sqlite3
import gi
import os.path
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk

sqlfile = os.path.join(os.path.dirname(__file__), "../../../../share/ptbl/elems.db")
tabname = "elems"
id_col = "Properties"
val_col = "Value"
class ElemWindow(Gtk.Window):
    def __init__(self):
        self.popup = None
    def on_info_clicked(self, infos, sing, css, namebutt):
        conn = sqlite3.connect(sqlfile)
        c = conn.cursor()

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(bytes(css.encode()))

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        if self.popup is None:
            Tabs = ["Overview", "Thermal", "Crystal", "Electronic", "Electrical", "Nuclear"]
            self.notebook = Gtk.Notebook(name=namebutt[int(sing)])
            for i in range(len(Tabs)):
                exe_str = "select * from "+ Tabs[i] +" where Properties ="+ str(sing)
                c.execute(exe_str)
                jour_name = c.fetchone()
                jour_name = list(jour_name)
                prps = [["Symbol", "Atomic Number",
                        "Atomic Weight", "Valence", "Electronegativity", "Electron Affinity(kJ/mol)"],
                        ["Phase", "Absolute Melting Point", "Absolute Boiling Point",
                         "Critical Pressure", "Critical Temperature", "Heat of Fusion", "Heat of Vaporization",
                         "Specific Heat", "Adiabetic Index", "Neel Point", "Curie Point"],
                        ["Atomic Radius (&#8491;)", "Covalent Radius (&#8491;)", "Van der Waals Radius (&#8491;)",
                         "Crystal Structure", "Lattice Parameter(a) (&#8491;)",
                         "Lattice Parameter(b) (&#8491;)", "Lattice Parameter(c) (&#8491;)", "Space Group Name",
                         "Space Group Number"],
                        ["Electron Configuration", "Magnetic Type",
                         "Mass Magnetic Susceptibility", "Molar Magnetic Susceptibility"],
                        ["Electrical Type", "Electrical Conductivity", "Resistivity",
                         "Superconducting Point"],
                        ["Half Life", "Life Time", "Decay Mode", "Quantum Numbers",
                         "Nuclear Cross Section", "Neytron Mass Absorption"]
                        ]
                elemprops = zip(prps[i], jour_name[2:])
                self.grid = Gtk.Grid(name=namebutt[int(sing)])
                self.grid.set_column_homogeneous(True)
                # self.grid.set_row_homogeneous(True)

                # Liststore
                self.liststore = Gtk.ListStore(str, str)
                for vals in elemprops:
                    self.liststore.append(vals)
                self.current_filter_language = None

                self.language_filter = self.liststore.filter_new()
                self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
                for q, column_title in enumerate(["Properties", "Values"]):
                    renderer = Gtk.CellRendererText()
                    column = Gtk.TreeViewColumn(column_title, renderer, markup=q)
                    self.treeview.append_column(column)
                self.scrollable_treelist = Gtk.ScrolledWindow()
                self.scrollable_treelist.set_vexpand(True)
                self.grid.attach(self.scrollable_treelist, 0, 0, 8, 20)
                self.scrollable_treelist.add(self.treeview)
                self.notebook.append_page(self.grid, Gtk.Label(Tabs[i]))

            popheader = Gtk.HeaderBar(name=namebutt[int(sing)])
            popheader.set_title(jour_name[1]+"-"+str(sing))
            popheader.set_show_close_button(True)

            self.popup = Gtk.Window(name=namebutt[int(sing)])
            self.popup.set_border_width(2)
            self.popup.set_default_size(450, 350)
            self.popup.set_titlebar(popheader)
            self.popup.add(self.notebook)

        self.popup.present()
        self.popup.show_all()
