import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class newProj(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="New Project")

        mainBox = self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        topBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        topBox.set_homogeneous(False)
        
        midOneBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midOneBox.set_homogeneous(False)

        midTwoBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midTwoBox.set_homogeneous(False)
        
        botBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        botBox.set_homogeneous(False)

        mainBox.pack_start(topBox, True, True, 10)
        mainBox.pack_start(midOneBox, True, True, 10)
        mainBox.pack_start(midTwoBox, True, True, 10)
        mainBox.pack_start(botBox, True, True, 10)

        label = Gtk.Label("Create a new project.")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)

        nameLabel = Gtk.Label("Project Name")
        nameLabel.set_justify(Gtk.Justification.CENTER)
        midOneBox.pack_start(nameLabel, True, True, 10)
        
        nameEntry = Gtk.Entry()
        nameEntry.set_text("Name")
        midOneBox.pack_start(nameEntry, True, True, 10)

        desLabel = Gtk.Label("Description")
        desLabel.set_justify(Gtk.Justification.CENTER)
        midTwoBox.pack_start(desLabel, True, True, 10)

        desEntry = Gtk.Entry()
        desEntry.set_text("Description")
        midTwoBox.pack_start(desEntry, True, True, 10)

        self.create = Gtk.Button(label="Create")
        self.create.connect("clicked", self.create_clicked)
        botBox.pack_start(self.create, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def create_clicked(self,widget):
        print("Create")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()


        