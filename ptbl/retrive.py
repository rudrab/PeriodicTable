#!/usr/bin/env python3
from gi.repository import Gtk
import sqlite3 as lite
import sys
import os
import numpy as np
#  import matplotlib.pyplot as plt
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
        ind = []; val = []; name = []
        with con:
            cur = con.cursor()
            cstr ="SELECT * from "+ table
            cur.execute(cstr)
            while True:
                #  names = row[1]
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
                    name.append(str(row[1]))
                except ValueError:
                    name.append(str(row[1]))
                    ind.append(int(row[0]))
                    val.append("NaN")

        x = np.array(ind).astype(np.double)
        y = np.array(val).astype(np.double)


        # Plot
        # plt.style.use('ptbl')
        p_window = Gtk.Window()
        p_window.set_default_size(750,500)
        p_header = Gtk.HeaderBar()
        p_window.set_titlebar(p_header)
        p_header.set_subtitle("Periodic Table")
        p_header.set_title(column)
        p_header.set_show_close_button(True)
        c = np.random.randint(1,50,size=120)
        #  norm = plt.Normalize(1,4)
        #  cmap = plt.cm.RdYlGn
        #  fig,ax = plt.subplots()
        #  sc = plt.scatter(x,y)
        #  plt.plot(x,y)
        fig = Figure(figsize=(10,6), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_ylabel(column, fontsize=20)
        ax.set_xlabel("Atomic Number")
        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                     ax.get_xticklabels() + ax.get_yticklabels()):
          item.set_fontsize(14)
          item.set_fontweight("bold")
        for axis in ['top','bottom','left','right']:
          ax.spines[axis].set_linewidth(2.5)
        ax.grid(True)
        ax.set_xticks([1, 11, 19, 37, 55, 87])
        sc=ax.scatter(x,y)
        ax.plot(x,y,"-")
        annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"), weight="bold", color="#ffffff")
        annot.set_visible(False)


        def update_annot(ind):
          pos = sc.get_offsets()[ind["ind"][0]]
          annot.xy = pos
          namel = (str([name[n] for n in ind["ind"]]))
          vall = str([val[n] for n in ind["ind"]])
          text = "{}, {}".format(namel[2:-2], vall[1:-1])
          annot.set_text(text)
          annot.get_bbox_patch().set_facecolor("#5777C0")
          annot.get_bbox_patch().set_alpha(0.9)


        def hover(event):
          vis = annot.get_visible()
          if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
              update_annot(ind)
              annot.set_visible(True)
              fig.canvas.draw_idle()
            else:
              if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
        canvas = FigureCanvas(fig)
        fig.canvas.mpl_connect("motion_notify_event", hover)

        sw = Gtk.ScrolledWindow()
        p_window.add(sw)

        canvas.set_size_request(750,500)
        sw.add_with_viewport(canvas)
        p_window.show_all()
