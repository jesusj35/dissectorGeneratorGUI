import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import workspaceLaunch
import newProject
import dissectorScript
import pimport
import export
import views 
import pcap

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")
        
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        headerButtonsBox = Gtk.Box(spacing=10)
        headerButtonsBox.set_homogeneous(False)
        
        projectViewBox = Gtk.Box(False,100)
        projectViewBox.set_size_request(100,500)
        projectViewBox.set_homogeneous(False)
        
        areaViews = Gtk.Notebook()
        self.add(areaViews)

        packetStreamBox = Gtk.Box(spacing=10)
        packetStreamBox.set_homogeneous(False)
        packetStreamBox.set_border_width(10)
        packetStreamBox.add(Gtk.Label('Default Page!'))
        areaViews.append_page(packetStreamBox, Gtk.Label('Packet Stream Area View'))

        dissectedStreamBox = Gtk.Box(spacing=10)
        dissectedStreamBox.set_homogeneous(False)
        dissectedStreamBox.set_border_width(10)
        dissectedStreamBox.add(Gtk.Label('Default Page!'))
        areaViews.append_page(dissectedStreamBox, Gtk.Label('Dissected Stream Area View'))

        rawDataBox = Gtk.Box(spacing=10)
        rawDataBox.set_homogeneous(False)
        rawDataBox.set_border_width(10)
        rawDataBox.add(Gtk.Label('Default Page!'))
        areaViews.append_page(rawDataBox, Gtk.Label('Raw Data Area'))

        consoleBox = Gtk.Box(spacing=10)
        consoleBox.set_homogeneous(False)
        consoleBox.set_border_width(10)
        consoleBox.add(Gtk.Label('No error message to show\n'
        '\n'
        '\n'
        '\n'
        '\n'
        '\n'))
        areaViews.append_page(consoleBox, Gtk.Label('Console Area'))

        mainBox.pack_start(headerButtonsBox, False, False, 10)
        mainBox.pack_start(projectViewBox, False, False, 10)
        mainBox.pack_start(areaViews, False, False, 10)

        self.button1 = Gtk.Button(label="Create Project")
        self.button1.connect("clicked", self.on_button1_clicked)
        headerButtonsBox.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Save Project")
        self.button2.connect("clicked", self.on_button2_clicked)
        headerButtonsBox.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="Close Project")
        self.button3.connect("clicked", self.on_button3_clicked)
        headerButtonsBox.pack_start(self.button3, True, True, 0)
        
        self.button4 = Gtk.Button(label="Switch Workspace")
        self.button4.connect("clicked", self.on_button4_clicked)
        headerButtonsBox.pack_start(self.button4, True, True, 0)

        self.button5 = Gtk.Button(label="Import Project")
        self.button5.connect("clicked", self.on_button5_clicked)
        headerButtonsBox.pack_start(self.button5, True, True, 0)

        self.button6 = Gtk.Button(label="Export Project")
        self.button6.connect("clicked", self.on_button6_clicked)
        headerButtonsBox.pack_start(self.button6, True, True, 0)

        self.button7 = Gtk.Button(label="Generate Dissector Script")
        self.button7.connect("clicked", self.on_button7_clicked)
        headerButtonsBox.pack_start(self.button7, True, True, 0)

        self.button8 = Gtk.Button(label="Organize Views")
        self.button8.connect("clicked", self.on_button8_clicked)
        headerButtonsBox.pack_start(self.button8, True, True, 0)

        self.button9 = Gtk.Button(label="Open PCAP")
        self.button9.connect("clicked", self.on_button9_clicked)
        headerButtonsBox.pack_start(self.button9, True, True, 0)

        # NAVIGATOR 
      
        # create a TreeStore with one string column to use as the model
        store = Gtk.TreeStore(str)
      
        # add row
        row1 = store.append(None, ['Project 1               '])
        
        #add child rows
        store.append(row1,['dissector1'])
        store.append(row1,['pcap1'])
        
        # add another row
        row2 = store.append(None, ['Project 2               '])
        store.append(row2,['dissector2'])
        store.append(row2,['pcap2'])
        
        # create the TreeView using treestore
        treeview = Gtk.TreeView(store)
        tvcolumn = Gtk.TreeViewColumn('Project')
        treeview.append_column(tvcolumn)
            
        cell = Gtk.CellRendererText()
        tvcolumn.pack_start(cell, True)
        tvcolumn.add_attribute(cell, 'text', 0)
        projectViewBox.add(treeview)


        #VIEWS FROM THE SIX

       



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
        win = pcap.Pcap()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()