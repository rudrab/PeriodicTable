#!/usr/bin/env python3
from gi.repository import Gtk
import sqlite3 as lite
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
#Possibly this rendering backend is broken currently
# from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
# from matplotlib.backends.backend_gtk3 import FigureCanvasGTK3 as FigureCanvas

sqlfile = os.path.join(os.path.dirname(__file__), "../../../../share/ptbl/elems.db")

class plotter():
    def plot_trend(self, column0, column1, column):
        if column == "Atomic Radius":
            table = "Crystal"
        if column == "Covalent Radius":
            table = "Crystal"
        if column == "Van der Waals Radius":
            table = "Crystal"
        if column == "Electron Affinity":
            table = "Overview"
        con = lite.connect(sqlfile)
        ind = []; val = []
        with con:
            cur = con.cursor()
            cstr ="SELECT * from "+ table
            cur.execute(cstr)
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                if column == "Atomic Radius":
                    col = row[2]
                if column == "Covalent Radius":
                    col = row[3]
                if column == "Van der Waals Radius":
                    col = row[4]
                if column == "Electron Affinity":
                    col = row[7]
                try:
                    float(col)
                    ind.append(int(row[0]))
                    val.append(float(col))
                except ValueError:
                    ind.append(int(row[0]))
                    val.append("NaN")

        ind = np.array(ind).astype(np.double)
        val = np.array(val).astype(np.double)


        # Plot
        # plt.style.use('ptbl')
        p_window = Gtk.Window()
        p_window.set_default_size(750,500)
        p_header = Gtk.HeaderBar()
        p_window.set_titlebar(p_header)
        p_header.set_subtitle("Periodic Table")
        p_header.set_title(column)
        p_header.set_show_close_button(True)

        fig = Figure(figsize=(10,6), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_ylabel(column)
        ax.set_xlabel("Z")
        ax.plot(ind, val, "r-o")
        # plt.show()
        sw = Gtk.ScrolledWindow()
        p_window.add(sw)

        canvas = FigureCanvas(fig)
        canvas.set_size_request(400,400)
        sw.add_with_viewport(canvas)
        p_window.show_all()
