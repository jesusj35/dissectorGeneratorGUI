import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Wlauncher(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")

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

        label = Gtk.Label("Select a directory as a workspace:\n PDGS uses the workspace"
        "directory to store projects")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)
        
        self.entry = Gtk.Entry()
        self.entry.set_text("Workspace Directory Path")
        midBox.pack_start(self.entry, True, True, 10)

        self.browse = Gtk.Button(label="Browse")
        self.browse.connect("clicked", self.browse_clicked)
        midBox.pack_start(self.browse, True, True, 10)

        self.launch = Gtk.Button(label="Launch")
        self.launch.connect("clicked", self.launch_clicked)
        botBox.pack_start(self.launch, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def launch_clicked(self,widget):
        print("Launch")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()
    
    def browse_clicked(self, widget):
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

        

