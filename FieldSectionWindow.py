import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Demo")

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=12)
        self.add(hbox)

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

        label = Gtk.Label("                                                                                                               ")
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

        #self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
        ##self.connect("drag-data-get", self.on_drag_data_get)
        #self.connect("drag-data-received", self.on_drag_data_received)


    def on_drag_data_get(self, widget, drag_context, data, info, time):
        print("Hello There!")

        


    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        print("             ")

win = DragDropWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()