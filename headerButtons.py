import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import workspaceLaunch
import newProject
import dissectorScript
import pimport
import export
import views 
import pcap

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")
        
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)  # Main Box
        self.add(mainBox)

        headerButtonsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)  # Buttons Box
        headerButtonsBox.set_homogeneous(False)

        mBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)   # Controls Middle Boxes
        
        projectViewBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)  # Project Nav Box
        projectViewBox.set_size_request(100,500)
        projectViewBox.set_homogeneous(True)

        mBox.pack_start(projectViewBox, True, True, 5)   # Packs Project View into mBox
        
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

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=12)  # Builder Box
        self.add(hbox)

        mBox.pack_start(hbox, True, True, 6)   # Packs Builder Box into middle box

        constructs = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)       
        constructs2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)      
        constructs3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)      
        constructs4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        dropArea = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)         


        hbox.pack_start(dropArea, True, True, 5)
        hbox.pack_start(constructs, True, True, 5)
        hbox.pack_start(constructs2, True, True, 5)
        hbox.pack_start(constructs3, True, True, 5)
        hbox.pack_start(constructs4, True, True, 5)

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
        mainBox.pack_start(mBox, False, False, 10)
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


        #DRAG AND DROP AREA 

       

        label = Gtk.Label("                                                                                                                                                                      ")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        labelField = Gtk.Label("Field")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        labelField2 = Gtk.Label("Field")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        field1 = Gtk.Button.new_with_label("Field (1 Byte)")
        field2 = Gtk.Button.new_with_label("Field (2 Byte)")
        field4 = Gtk.Button.new_with_label("Field (4 Byte)") 
        field8 = Gtk.Button.new_with_label("Field (8 Byte)")
        field16 = Gtk.Button.new_with_label("Field (16 Byte)")
        

        start = Gtk.Button.new_with_label("Start Field")
        end = Gtk.Button.new_with_label("End Field")
        reference = Gtk.Button.new_with_label("Reference List")
        packet = Gtk.Button.new_with_label("Packet Info")
        fieldV = Gtk.Button.new_with_label("Field (var size)") 

        labelDes = Gtk.Label("Decision")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        expression = Gtk.Button.new_with_label("Expression")

        labelCon = Gtk.Label("Connectors")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        con = Gtk.Button.new_with_label("----->")

        labelOp = Gtk.Label("Operators")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        labelOp2 = Gtk.Label("Operators")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        less = Gtk.Button.new_with_label("<")
        greater = Gtk.Button.new_with_label(">")
        lessEq = Gtk.Button.new_with_label("<=")
        greaterEq = Gtk.Button.new_with_label(">=")
        equal = Gtk.Button.new_with_label("==")
        xor = Gtk.Button.new_with_label("~=")

        andop = Gtk.Button.new_with_label("And")
        orop = Gtk.Button.new_with_label("Or")
        notop = Gtk.Button.new_with_label("Not")
        operand = Gtk.Button.new_with_label("Operand")
        
        constructs.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)   # Sets constructs box as source
        dropArea.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)                # Sets dropArea box as destination
        
        constructs.connect("drag-data-get", self.on_drag_data_get)                   # Handles drag function
        constructs.connect("drag-data-get", self.on_drag_data_get)   
        dropArea.connect("drag-data-received", self.on_drag_data_received)           # Handles drop function

        constructs.pack_start(labelField, True, True, 5)
        constructs.pack_start(field1, True, True, 5)
        constructs.pack_start(field2, True, True, 5)
        constructs.pack_start(field4, True, True, 5)
        constructs.pack_start(field8, True, True, 5)
        constructs.pack_start(field16, True, True, 5)

        constructs2.pack_start(labelField2, True, True, 5)
        constructs2.pack_start(fieldV, True, True, 5)
        constructs2.pack_start(start, True, True, 5)
        constructs2.pack_start(end, True, True, 5)
        constructs2.pack_start(reference, True, True, 5)
        constructs2.pack_start(packet, True, True, 5)

        constructs3.pack_start(labelDes, True, True, 5)
        constructs3.pack_start(expression, True, True, 5)
        constructs3.pack_start(labelCon, True, True, 5)
        constructs3.pack_start(con, True, True, 5)
        constructs3.pack_start(labelOp, True, True, 5)
        constructs3.pack_start(less, True, True, 5)
        constructs3.pack_start(greater, True, True, 5)
        constructs3.pack_start(lessEq, True, True, 5)
        constructs3.pack_start(greaterEq, True, True, 5)
        constructs3.pack_start(equal, True, True, 5)
        constructs3.pack_start(xor, True, True, 5)

        constructs4.pack_start(labelOp2, True, True, 5)
        constructs4.pack_start(andop, True, True, 5)
        constructs4.pack_start(orop, True, True, 5)
        constructs4.pack_start(notop, True, True, 5)
        constructs4.pack_start(operand, True, True, 5)

       



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
   
    def on_drag_data_get(self, widget, drag_context, data, info, time):
        print("Hello There!")

    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        print("             ")
        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()