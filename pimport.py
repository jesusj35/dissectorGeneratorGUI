import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class Pimport(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Import")

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

        label = Gtk.Label("Import a project into the current workspace.")
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

        self.projectIm = Gtk.Button(label="Import")
        self.projectIm.connect("clicked", self.projectIm_clicked)
        botBox.pack_start(self.projectIm, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def browse_clicked(self,widget):
        print("Browse")

    def projectIm_clicked(self,widget):
        print("Launch")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()
        
