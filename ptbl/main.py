import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk, GLib
import ptbl.elem_H as elem_H
import ptbl.veggards as vegards
import ptbl.retrive as plotter
import ptbl.dialogue as dialogue
# import ptbl.elem_H as elem_H
import sys
import os

data_dir = os.path.join(GLib.get_user_data_dir(), "ptbl")
col = [['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'He'],
       ['Li', 'Be', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'Ne'],
       ['Na', 'Mg', '', '', '', '', '', '', '', '', '', '', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
       ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
       ['Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
       ['Cs', 'Ba', 'La',
        "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
        'Hf', 'Ta', 'W', 'Re', 'Os', 'It', 'Pt', 'Au', 'Hg', 'Ti', 'Pb', 'Bi',  'Po', 'At', 'Rn'],
       ['Fr', 'Ra', 'Ac',
        "Th", "Pa", "U", "Np", "Pu", "Am", "Cu", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
        "Rf", "Db", "Sg", "Bh", 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
       ]

full_col = ["Hydrogen"    , "Helium"      , "Lithium"     , "Beryllium"  , "Boron"        , "Carbon"        ,
            "Nitrogen"    , "Oxygen"      , "Fluorine"    , "Neon"       , "Sodium"       , "Magnesium"     , "Aluminum"   ,
            "Silicon"     , "Phosphorus	" , "Sulfur"      , "Chlorine"   , "Argon"        , "Potassium"     , "Calcium"    ,
            "Scandium"    , "Titanium	"   , "Vanadium"    , "Chromium"   , "Manganese"    , "Iron"          , "Cobalt"     ,
            "Nickel"      , "Copper"      , "Zinc"        , "Gallium"    , "Germanium"    , "Arsenic"       ,
            "Selenium"    , "Bromine"     , "Krypton"     , "Rubidium"   , "Strontium"    , "Yttrium"       , "Zirconium"  ,
            "Niobium"     , "Molybdenum"  , "Technetium"  , "Ruthenium"  , "Rhodium"      , "Palladium"     ,
            "Silver"      , "Cadmium"     , "Indium"      , "Tin"        , "Antimony"     , "Tellurium"     , "Iodine"     ,
            "Xenon"       , "Cesium"      , "Barium"      , "Lanthanum"  , "Cerium"       , "Praseodymium"  , "Neodymium"  ,
            "Promethium"  , "Samarium"    , "Europium"    , "Gadolinium" , "Terbium"      , "Dysprosium"    ,
            "Holmium"     , "Erbium"      , "Thulium"     , "Ytterbium"  , "Lutetium"     , "Hafnium"       ,
            "Tantalum"    , "Tungsten"    , "Rhenium"     , "Osmium"     , "Iridium"      , "Platinum"      , "Gold"       ,
            "Mercury"     , "Thallium"    , "Lead"        , "Bismuth"    , "Polonium"     , "Astatine"      , "Radon"      ,
            "Francium"    , "Radium"      , "Actinium"    , "Thorium"    , "Protactinium" , "Uranium"       ,
            "Neptunium"   , "Plutonium"   , "Americium"   , "Curium"     , "Berkelium"    , "Californium"   ,
            "Einsteinium" , "Fermium"     , "Mendelevium" , "Nobelium"   , "Lawrencium"   , "Rutherfordium" ,
            "Dubnium"     , "Seaborgium"  , "Bohrium"     , "Hassium"    , "Meitnerium"   , "Darmstadtium"  ,
            "Roentgenium" , "Copernicum"  , "Nihonium"    , "Flerovium"  , "Moscovium"    , "Livermorium"   , "Tennessine" ,
            "Oganesson"]

class GridWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application = app,
                            default_width=1000,
                            default_height=200,
                            border_width=2,
                            name = "MyWindow")
        # Importing the libs
        self.Vegards = vegards.vegards()
        self.Plotter = plotter.plotter()
        self.Messages = dialogue.MessageDialog()

        self.headerbar = Gtk.HeaderBar()
        self.set_titlebar(self.headerbar)
        self.headerbar.set_show_close_button(True)
        self.main_header = "Periodic Table"
        self.headerbar.set_title(self.main_header)
        icontheme = Gtk.IconTheme.get_default()
        self.icon = icontheme.load_icon("ptbl", 64, 0)

        utility_action = Gio.SimpleAction.new("utility", None)
        utility_action.connect("activate", self.Messages.utility_activated)
        self.add_action(utility_action)
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.Messages.about_activated)
        self.add_action(about_action)

        # Menu using Gio
        h_grid = Gtk.Grid()
        UtilButton = Gtk.MenuButton()
        UtilButton.props.label = "Utility"
        utilmenu = Gio.Menu()
        plt_atrad = Gio.Menu()
        utilmenu.append("Vegard's Law", "win.veggard")
        utilmenu.append_submenu("Plot", plt_atrad)
        plt_atrad.append("Atomic Radius", "win.atrad")
        plt_atrad.append("Covalent Radius", "win.covrad")
        plt_atrad.append("Van der Waals Radius", "win.vdwrad")
        plt_atrad.append("Electron Affinity", "win.eleaff")
        utilmenu.append("Quit", "app.quit")
        h_grid.attach(UtilButton, 0, 0, 3, 1)
        UtilButton.set_menu_model(utilmenu)
        self.headerbar.pack_start(h_grid)

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.Messages.about_activated)

        # Open menu
        vegard_menu = Gio.SimpleAction.new("veggard", None)
        vegard_menu.connect("activate", self.Vegards.vegard_clicked)
        self.add_action(vegard_menu)
        atrad_menu = Gio.SimpleAction.new("atrad", None)
        atrad_menu.connect("activate", self.Plotter.plot_trend, "Atomic Radius")
        self.add_action(atrad_menu)
        covrad_menu = Gio.SimpleAction.new("covrad", None)
        covrad_menu.connect("activate", self.Plotter.plot_trend, "Covalent Radius")
        self.add_action(covrad_menu)
        vdwrad_menu = Gio.SimpleAction.new("vdwrad", None)
        vdwrad_menu.connect("activate", self.Plotter.plot_trend, "Van der Waals Radius")
        self.add_action(vdwrad_menu)
        eleaff_menu = Gio.SimpleAction.new("eleaff", None)
        eleaff_menu.connect("activate", self.Plotter.plot_trend, "Electron Affinity")
        self.add_action(eleaff_menu)

        # Check or Create data_dir
        if not os.path.isdir(data_dir):
          os.mkdir(data_dir)

        style_provider = Gtk.CssProvider()
        css = """
        #AlkMet{
            background: #795548;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #AlkMet:hover{
            background:#A1887F;
                }
        #AlkEat{
            background: #4CAF50;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #AlkEat:hover{
            background:#81C784;
                }
        #TranMet{
            background: #5C6BC0;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", sans-serif;
            }
        #TranMet:hover{
            background:#9FA8DA;
                }
        #PostT{
            background: #009688;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #PostT:hover{
            background:#4DB68C;
                }
        #Metaloids{
            background: #FF9800;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #Metaloids:hover{
            background:#FFB74D;
                }
        #Gases{
            background: #BA68C8;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #Gases:hover{
            background:#CE93D8;
                }
        #LanBut{
            background: #EC407A;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #LanBut:hover{
            background:#F48FB1;
                }
        #ActBut{
            background: #8D6E63;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #ActBut:hover{
            background:#BCAAA4;
                }
        #Halos{
            background: #2979FF;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #Halos:hover{
            background:#82B1FF;
                }
        #EntGas{
            background: #607D8B;
            border-radius: 5px;
            border-color: #000;
            margin: 2px;
            color: white;
            font-family: "Roboto Light", serif;
            }
        #EntGas:hover{
            background:#90A4AE;
                }
        """
        namebutt = [""]*120
        namebutt[1] = namebutt[6] = namebutt[7] = namebutt[8] = namebutt[15] = namebutt[16] = namebutt[34] ="Gases"
        namebutt[9] = namebutt[17] = namebutt[35] = namebutt[53] = namebutt[85] = namebutt[117]  ="Halos"
        namebutt[13] = namebutt[31] = namebutt[49] = namebutt[50] = namebutt[81] = namebutt[82] = namebutt[83] = namebutt[113] = namebutt[114] = namebutt[115] = namebutt[116] ="PostT"
        namebutt[5] = namebutt[14] = namebutt[32] = namebutt[33] = namebutt[51] = namebutt[52] = namebutt[84] ="Metaloids"
        namebutt[2] = namebutt[10] = namebutt[18] = namebutt[36] = namebutt[54] = namebutt[86] = namebutt[118] ="EntGas"
        namebutt[3] = namebutt[11] = namebutt[19] = namebutt[37] = namebutt[55] = namebutt[87] = "AlkMet"
        namebutt[4] = namebutt[12] = namebutt[20] = namebutt[38] = namebutt[56] = namebutt[88] = "AlkEat"
        for i in range(57,72):
            namebutt[i]="LanBut"
        for i in range(89,104):
            namebutt[i]="ActBut"
        for i in range(104,113):
            namebutt[i]="TranMet"
        for i in range(72,81):
            namebutt[i]="TranMet"
        for i in range(39,49):
            namebutt[i]="TranMet"
        for i in range(21,31):
            namebutt[i]="TranMet"
        style_provider.load_from_data(bytes(css.encode()))

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        grid = Gtk.Grid()
        el_count = 0
        re_count = 0
        button = []
        button.append("")
        for cols in range(len(col)):
            for elems in col[cols]:
                if not elems == "":
                    el_count += 1
                    blabel = ""
                    if el_count in range(1, 58):
                        button.append(Gtk.Button(label=blabel, name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems),cols,1,1)
                    elif el_count in range(57, 72):
                        button.append(Gtk.Button(label=blabel, name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems),cols+8,1,1)
                    elif el_count in range(72, 87):
                        button.append(Gtk.Button(label=blabel, name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems)-14,cols,1,1)
                    elif el_count in range(87,90):
                        button.append(Gtk.Button(label=blabel, name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems),cols,1,1)
                    elif el_count in range(89, 104):
                        button.append(Gtk.Button(label=blabel,name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems),cols+8,1,1)
                    elif el_count in range(104, 120):
                        button.append(Gtk.Button(label=blabel, name=namebutt[el_count]))
                        grid.attach(button[el_count], col[cols].index(elems)-14,cols,1,1)
                    label = button[el_count].get_child()
                    label.set_markup("<b>"+str(elems)+"</b>\n<small>"+str(el_count)+"</small>")
                    label.set_justify(2)
                    button[el_count].connect("clicked", elem_H.ElemWindow().on_info_clicked, str(el_count), css, namebutt)
                    button[el_count].set_tooltip_text(full_col[el_count-1])
        empty = Gtk.Label("")
        #  for i in range(120):
          #  butto
        grid.attach(empty,0,7,1,1)
        self.add(grid)
class ptbl(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)
        self.Messages = dialogue.MessageDialog()

    def do_activate(self):
        win = GridWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        action = Gio.SimpleAction(name="utility")
        action.connect("activate", self.Messages.utility_activated)
        self.add_action(action)
        action = Gio.SimpleAction(name="settings")
        action.connect("activate", self.Messages.settings)
        self.add_action(action)
        action = Gio.SimpleAction(name="about")
        action.connect("activate", self.Messages.about_activated)
        self.add_action(action)
        action = Gio.SimpleAction(name="quit")
        action.connect("activate", lambda a, b: self.quit())
        self.add_action(action)


        builder = Gtk.Builder()
        builder.add_from_file(os.path.join(os.path.dirname
                                           (__file__), '../../../../share/ptbl/ui/menubar.ui'))

        self.set_app_menu(builder.get_object("app-menu"))
        self.set_accels_for_action("win.utility", ["<Primary>u"])
        self.set_accels_for_action("win.about", ["<Primary>h"])

app = ptbl()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
