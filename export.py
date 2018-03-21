import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class pExport(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Export")

        mainBox = self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        topBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        topBox.set_homogeneous(False)
        
        midBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midBox.set_homogeneous(False)

        midTwoBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midTwoBox.set_homogeneous(False)
        
        botBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        botBox.set_homogeneous(False)

        mainBox.pack_start(topBox, True, True, 10)
        mainBox.pack_start(midBox, True, True, 10)
        mainBox.pack_start(midTwoBox, True, True, 10)
        mainBox.pack_start(botBox, True, True, 10)

        label = Gtk.Label("Export a project to local.")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)
        
        plabel = Gtk.Label("Project")
        plabel.set_justify(Gtk.Justification.CENTER)
        midBox.pack_start(plabel, True, True, 10)

        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        midBox.pack_start(self.entry, True, True, 10)

        self.browse = Gtk.Button(label="Browse")
        self.browse.connect("clicked", self.browse_clicked)
        midBox.pack_start(self.browse, True, True, 10)

        plabel = Gtk.Label("Export")
        plabel.set_justify(Gtk.Justification.CENTER)
        midTwoBox.pack_start(plabel, True, True, 10)

        self.entry = Gtk.Entry()
        self.entry.set_text("System Path")
        midTwoBox.pack_start(self.entry, True, True, 10)

        self.browse2 = Gtk.Button(label="Browse")
        self.browse2.connect("clicked", self.browse2_clicked)
        midTwoBox.pack_start(self.browse2, True, True, 10)

        self.export = Gtk.Button(label="Export")
        self.export.connect("clicked", self.export_clicked)
        botBox.pack_start(self.export, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def browse_clicked(self,widget):
        print("Browse")
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def browse2_clicked(self,widget):
        print("Browse")
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def export_clicked(self,widget):
        print("Launch")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()
        
