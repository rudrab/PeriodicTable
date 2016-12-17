import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk
import re
import sqlite3
import ptbl.dialogue as dialogue
import numpy as np

sqlfile = os.path.join(os.path.dirname(__file__), "../../../../share/ptbl/elems.db")


class vegards(Gtk.Window):
    def __init__(self):
        self.opt_vol_stat = None
    def vegard_clicked(self, str1, str2):
        self.veg = Gtk.Window()
        self.veg.set_default_size(6,4)
        self.veg.set_border_width(4)
        header = Gtk.HeaderBar()
        self.veg.set_titlebar(header)
        header.set_title("Vegards Law for Binary Alloy")
        header.set_subtitle("Periodic Table")
        header.set_show_close_button(True)

        self.Messages = dialogue.MessageDialog()

        self.Vgrid = Gtk.Grid()
        self.Vgrid.set_column_spacing(5)
        self.Vgrid.set_row_spacing(5)
        self.Vgrid.set_border_width(5)
        # self.Vgrid.set_column_homogeneous(True)
        self.veg.add(self.Vgrid)
        self.entry = Gtk.Entry()
        self.entry.set_text("A50B50")
        alloy = Gtk.Label("Alloy")
        self.entry.connect("activate", self.entry_text)

        self.Vgrid.attach(self.entry, 1, 0, 1,1)
        self.Vgrid.attach(alloy, 0, 0, 1, 1)
        # self.Vgrid.attach(self.a_label, 1, 1, 1, 1)

        self.veg.show_all()

    def entry_text(self, widget):
        self.text = self.entry.get_text()
        self.a_label = Gtk.Label("Alloy")
        name = ""
        self.alloy = Gtk.Label()
        self.alloy.set_markup("")
        # self.alloy.show()
        Gtk.Grid.remove_row(self.Vgrid, 1)
        m = re.findall(r'(\D*)(\d+)', self.text)
        conc = []
        for i in range(len(m)):
            name = name + m[i][0]+"<sub>"+m[i][1]+"</sub>"
        if sum(float(item[1]) for item in m) != 100.:
            substr = "Total composition %s is not 100" %"+".join( [item[i]for item in m])
            self.Messages.on_error_clicked("Wrong Composition",substr)
            return
        get_datab.data(self, m)
        if self.data_stat == -1:
            return

        # Now Calculate the Parameters
        # Lattice Parameters
        # \average(\sum(latpar(x)*conc))
        res = []
        for i in range(len(m)):
            res.append([j * float(m[i][1])/100. for j in self.latpar[i]])
        self.lat_alloy = []
        for i in range(len(res[0])):
            self.lat_alloy.append(round(sum(j[i] for j in res),4))

        # Atomic Weight
        res = []
        for i in range(len(m)):
            res.append(float(self.weight[i])*float(m[i][1])/100.)
        weight_alloy = round(sum(res),4)
        l_lat_alloy = Gtk.Label(self.lat_alloy)
        l_wei_alloy = Gtk.Label(weight_alloy)

        self.alloy.set_markup(name)
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        self.Vgrid.attach(separator, 0, 2, 4, 1)

        # Create and write to GUI
        # Print lattice infos
        info_group1 = Gtk.Label()
        info_group1.set_markup("<b>Lattice</b>")

        self.Vgrid.attach(info_group1, 0, 2, 1, 1)
        self.Vgrid.attach(Gtk.Label("Element"), 0, 3, 1, 1)
        self.Vgrid.attach(Gtk.Label("Atomic Weight"), 1, 3, 1, 1)
        self.Vgrid.attach(Gtk.Label("Lattice Parameters"), 2, 3, 1, 1)
        self.Vgrid.attach(Gtk.Label("%"), 3, 3, 1, 1)


        lelem = []; llat = []; lwei = []; lpar = []
        for i in range(len(m)):
            lelem.append(Gtk.Label(m[i][0]))
            llat.append(Gtk.Label(str(self.latpar[i])))
            lwei.append(Gtk.Label(str(self.weight[i])))
            lpar.append(Gtk.Label(str(m[i][1])))
            self.Vgrid.attach(lelem[i], 0, 4+i, 1, 1)
            self.Vgrid.attach(llat[i],  2, 4+i, 1, 1)
            self.Vgrid.attach(lwei[i],  1, 4+i, 1, 1)
            self.Vgrid.attach(lpar[i],  3, 4+i, 1, 1)
            self.row_num = 4+i

        lat_var = Gtk.Button.new_with_label("Lattice optimization with fixed volume")
        lat_var.connect("clicked", self.vol_conv_lat_var)
        # self.vol_conv_lat_var(self.lat_alloy, self.row_num)
        # Print alloy infos
        info_alloy = Gtk.Label()
        info_alloy.set_markup("<b>Alloy</b>")
        self.Vgrid.attach(info_alloy, 0,   self.row_num+1, 1, 1)
        self.Vgrid.attach(self.alloy, 0,   self.row_num+2, 1, 1)
        self.Vgrid.attach(l_wei_alloy, 1,  self.row_num+2, 1, 1)
        self.Vgrid.attach(l_lat_alloy,  2, self.row_num+2, 1, 1)
        self.Vgrid.attach(lat_var, 0, self.row_num+3, 4, 1)
        self.Vgrid.show_all()


    def vol_conv_lat_var(self, widget):
    # volume conserved variation of lattice parameters
        if self.opt_vol_stat is None:
            opt_vol = self.lat_alloy[0]*self.lat_alloy[1]*self.lat_alloy[2]
            # varying x -5% to +5% with fixed volume
            # x /= y is not considered
            for xmul in range(-5,6):
                lp = []
                lp.append(round(self.lat_alloy[0]*((100.+xmul)/100.), 4))
                lp.append(round(self.lat_alloy[1]*((100.+xmul)/100.), 4))
                lp.append(round(opt_vol/(lp[0]*lp[1]), 4))
                per_label = Gtk.Label()
                per_label.set_markup("x ="+str(100+xmul)+"%")
                self.Vgrid.attach(per_label, 0, self.row_num+9+xmul, 1,1)
                self.Vgrid.attach(Gtk.Label(str(lp)), 2, self.row_num+9+xmul, 1,1)
        self.Vgrid.show_all()

class get_datab():
    def data(self, data):
        self.data_stat = 1
        conn = sqlite3.connect(sqlfile)
        c = conn.cursor()
        self.latpar = [[0 for x in range(3)] for y in range(len(data))]
        self.weight = [0  for x in range(len(data))]
        # Getting lattice parameters
        for i in range(len(data)):
            try:
                exe_str = "select Number from Overview where Symbol ='%s'" %str(data[i][0])
                # print(exe_str)
                c.execute(exe_str)
                atnum = c.fetchall()
                self.data_stat = ((atnum[0]))
            except:
                substr = "Is element %s is real?" %str(data[i][0])
                self.Messages.on_error_clicked("Wrong Elements",substr)
                self.data_stat = -1
                return
            for q in range(1,4):
                exe_str = "select latpar"+str(q)+" from Crystal where Properties ="+atnum[0][0]
                c.execute(exe_str)
                latp = c.fetchall()
                self.latpar[i][q-1]=float(latp[0][0])
            exe_str = "select Weight from Overview where Properties ="+atnum[0][0]
            c.execute(exe_str)
            wei = c.fetchall()
            self.weight[i] = (wei[0][0])


