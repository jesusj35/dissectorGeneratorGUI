import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class Pcap(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")

        mainBox = self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        topBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        topBox.set_homogeneous(False)
        
        midBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midBox.set_homogeneous(False)
        
        botBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        botBox.set_homogeneous(False)

        mainBox.pack_start(topBox, True, True, 10)
        mainBox.pack_start(midBox, True, True, 10)
        mainBox.pack_start(botBox, True, True, 10)

        label = Gtk.Label("Open a PCAP file.")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)
        
        plabel = Gtk.Label("PCAP Name")
        plabel.set_justify(Gtk.Justification.CENTER)
        midBox.pack_start(plabel, True, True, 10)

        self.entry = Gtk.Entry()
        self.entry.set_text("PCAP File")
        midBox.pack_start(self.entry, True, True, 10)

        self.browse = Gtk.Button(label="Browse")
        self.browse.connect("clicked", self.browse_clicked)
        midBox.pack_start(self.browse, True, True, 10)

        self.open = Gtk.Button(label="Open")
        self.open.connect("clicked", self.open_clicked)
        botBox.pack_start(self.open, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def browse_clicked(self,widget):
        print("Browse")
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def open_clicked(self,widget):
        print("Launch")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()
   
    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)
        