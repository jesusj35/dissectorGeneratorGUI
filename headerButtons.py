import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import workspaceLaunch
import newProject
import dissectorScript
import pimport
import export
import views 

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)


        self.button1 = Gtk.Button(label="Create Project")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Save Project")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Close Project")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)
        
        self.button4 = Gtk.Button(label="Switch Workspace")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)

        self.button5 = Gtk.Button(label="Import Project")
        self.button5.connect("clicked", self.on_button5_clicked)
        self.box.pack_start(self.button5, True, True, 0)

        self.button6 = Gtk.Button(label="Export Project")
        self.button6.connect("clicked", self.on_button6_clicked)
        self.box.pack_start(self.button6, True, True, 0)

        self.button7 = Gtk.Button(label="Generate Dissector Script")
        self.button7.connect("clicked", self.on_button7_clicked)
        self.box.pack_start(self.button7, True, True, 0)

        self.button8 = Gtk.Button(label="Organize Views")
        self.button8.connect("clicked", self.on_button8_clicked)
        self.box.pack_start(self.button8, True, True, 0)

        self.button9 = Gtk.Button(label="Open PCAP")
        self.button9.connect("clicked", self.on_button9_clicked)
        self.box.pack_start(self.button9, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Creating")
        proj = newProject.newProj()
        proj.connect("destroy", Gtk.main_quit)
        proj.show_all()
        Gtk.main()

    def on_button2_clicked(self, widget):
        print("Saving")
    
    def on_button3_clicked(self,widget):
        print("Closing")    
    
    def on_button4_clicked(self,widget):
        print("Switching")
        work = workspaceLaunch.Wlauncher()
        work.connect("destroy", Gtk.main_quit)
        work.show_all()
        Gtk.main()
        
    
    def on_button5_clicked(self,widget):
        print("Importing")
        win = pimport.Pimport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    
    def on_button6_clicked(self,widget):
        print("Exporting")
        win = export.pExport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_button7_clicked(self,widget):
        print("Generating")
        win = dissectorScript.newDissector()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_button8_clicked(self,widget):
        print("Organizing")
        win = views.Views()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_button9_clicked(self,widget):
        print("Opening")
        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


