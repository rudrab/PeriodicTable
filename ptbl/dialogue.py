###########################################
# dialogue.py
# Author: Rudra Banerjee
# Last Updated: 20/01/2016
#
# Various warning and Error dialogues
# License: GPLv3
###########################################
import gi
import ptbl
import os, pickle
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib
from gi.repository import GdkPixbuf
#  from gi.repository import Gtk, Gio

data_dir = os.path.join(GLib.get_user_data_dir(), "ptbl")
class MessageDialog(Gtk.Window):


    def on_info_clicked(self, info1, info2):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, info1)
        dialog.format_secondary_text(info2)
        dialog.run()
        dialog.destroy()

    def on_error_clicked(self, err_str1, err_str2):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
            Gtk.ButtonsType.OK, err_str1)
        dialog.format_secondary_text(err_str2)
        dialog.run()
        dialog.destroy()

    def on_warn_clicked(self, err_str1, err_str2):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
            Gtk.ButtonsType.OK, err_str1)
        dialog.format_secondary_text(err_str2)
        response = dialog.run()
        dialog.destroy()

    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
            Gtk.ButtonsType.YES_NO, "This is an QUESTION MessageDialog")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        response = dialog.run()
        if response == Gtk.ResponseType.YES:
            print("QUESTION dialog closed by clicking YES button")
        elif response == Gtk.ResponseType.NO:
            print("QUESTION dialog closed by clicking NO button")

        dialog.destroy()

    def about_activated(self, action, data=None):
        copyright = "Copyright \u00a9 2016- - Rudra Banerjee"
        comments = "Periodic Table"
        dialog = Gtk.AboutDialog(program_name="Periodic Table", transient_for=self,
                                 name="About Periodic Table",
                                 comments=comments,
                                 version= ptbl.version,
                                 copyright=copyright,
                                 license_type=Gtk.License.GPL_3_0,
                                 authors=(["Rudra Banerjee"]),
                                 website="https://rudrab.github.io/PeriodicTable/")
        # dialog.set_transient(Window)
        dialog.set_logo_icon_name("ptbl")
        # dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_size(
            # "mkbib.svg", 128, 128)
        # )
        dialog.run()
        dialog.destroy()

    def utility_activated(self, action,data=None):
        print("Utility Activated")

    def settings(self,err1, err2):
        self.config_file = os.path.join(data_dir,"config.dat")
        Wpref =  Gtk.Window(border_width=5)
        prefheader = Gtk.HeaderBar()
        prefheader.set_subtitle("Preferences")
        prefheader.set_title("Periodic Table")
        Wpref.set_titlebar(prefheader)
        prefheader.set_show_close_button(True)
        menuicon = Gtk.Image.new_from_icon_name("preferences-desktop-symbolic", Gtk.IconSize.MENU);
        Gtk.HeaderBar.pack_start(prefheader,menuicon);

        Wpref.set_default_size(350, 350)
        grid = Gtk.Grid(column_spacing=20)
        Wpref.add(grid)
        dir_label = Gtk.Label("Materials-Project api key")
        self.user_dir =Gtk.Entry()
        #  if os.path.isfile(self.config_file) and os.path.getsize(self.config_file)>0:
          #  with shelve.open(self.config_file) as cnf:
            #  key = cnf['key']
          #  self.user_dir.set_text(key)
        #  else:
        self.user_dir.set_text("Material Project Key")
        #  print(data_dir)
        self.dir_button = Gtk.Button()
        self.dir_button.set_always_show_image(True)
        self.dir_button.set_image(image=Gtk.Image(
                icon_name="document-save-symbolic"))
        self.dir_button.set_image_position(1)
        self.dir_button.connect("clicked", self.dic_save_clicked)
        self.setting = Gio.Settings.new("org.example.ptbl")
        #  self.setting.bind("base-folder", self.user_dir, "label", Gio.SettingsBindFlags.DEFAULT)
        #  self.basedir = self.setting.get_value("api-key")
        # print("From"+str(self.basedir))
        grid.attach(dir_label, 0, 1, 1, 1)
        grid.attach(self.user_dir, 1, 1, 1, 1)
        grid.attach(self.dir_button, 2, 1, 2, 1)
        Wpref.show_all()

    def dic_save_clicked(self, name):
      mytdict = {"Key":"value"}
      self.keyval = self.user_dir.get_text()
      print(self.keyval)
      with open(self.config_file, "wb") as inf:
        mytdict.update({"Key":self.keyval})
        pickle.dump(mytdict, inf)

      vals = pickle.load(open(self.config_file, "rb"))
      print(vals)
      #  with open(self.config_file, "rb") as inf:
        #  pickle.load()

      #  with open(config_file, "wb") as cnf:

        #  pickle.dump()

# class PopWindow():
#     def popup(self):
#         self.popup = Gtk.Window()
#         self.popup.set_border_width(2)
#         self.popheader = Gtk.HeaderBar()
#         self.popup.set_titlebar(self.popheader)
#         # popheader.set_title(indx)
#         self.popup.set_default_size(450, 550)
#         self.popheader.set_show_close_button(True)



class FileDialog(Gtk.Window):
    # File Chooser
    # Open, Save
    def FileChooser(self, header, action,act_button):
        self.path = None
        self.dialog = Gtk.FileChooserDialog(header[0], self,
                                       action,
                                       (Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        act_button, Gtk.ResponseType.OK))
        if header[3]:
            filter = Gtk.FileFilter()
            filter.set_name(header[1])
            filter.add_pattern(header[2])
            self.dialog.add_filter(filter)
            filter = Gtk.FileFilter()
            filter.set_name("All Files")
            filter.add_pattern("*")
            self.dialog.add_filter(filter)

        self.response = self.dialog.run()

def close_window(self, widget):
    widget.destroy()





