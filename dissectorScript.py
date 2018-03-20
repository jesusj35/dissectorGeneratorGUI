import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class newDissector(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Script")

        mainBox = self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        topBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        topBox.set_homogeneous(False)
        
        midOneBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midOneBox.set_homogeneous(False)

        midTwoBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midTwoBox.set_homogeneous(False)

        midThreeBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        midThreeBox.set_homogeneous(False)
        
        botBox = self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        botBox.set_homogeneous(False)

        mainBox.pack_start(topBox, True, True, 10)
        mainBox.pack_start(midOneBox, True, True, 10)
        mainBox.pack_start(midTwoBox, True, True, 10)
        mainBox.pack_start(midThreeBox, True, True, 10)
        mainBox.pack_start(botBox, True, True, 10)

        label = Gtk.Label("Generate a custom dissector script from a selected project.")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)

        nameLabel = Gtk.Label("Project")
        nameLabel.set_justify(Gtk.Justification.CENTER)
        midOneBox.pack_start(nameLabel, True, True, 10)
        
        nameEntry = Gtk.Entry()
        nameEntry.set_text("Name")
        midOneBox.pack_start(nameEntry, True, True, 10)

        self.browse = Gtk.Button(label="Browse")
        self.browse.connect("clicked", self.browse_clicked)
        midOneBox.pack_start(self.browse, True, True, 10)

        nameLabel = Gtk.Label("Dissector Format")
        nameLabel.set_justify(Gtk.Justification.LEFT)
        midTwoBox.pack_start(nameLabel, True, True, 10)

        format_store = Gtk.ListStore(int,str)
        format_store.append([1, "format1"])
        format_store.append([2, "format2"])
        format_store.append([3, "format3"])
        format_store.append([4, "format4"])
        format_store.append([5, "format5"])
        
        format_combo = Gtk.ComboBox.new_with_model_and_entry(format_store)
        format_combo.connect("changed", self.on_name_combo_changed)
        format_combo.set_entry_text_column(1)
        midTwoBox.pack_start(format_combo, False, False, 20)

        nameLabel = Gtk.Label("Save Location")
        nameLabel.set_justify(Gtk.Justification.CENTER)
        midThreeBox.pack_start(nameLabel, True, True, 10)
        
        nameEntry = Gtk.Entry()
        nameEntry.set_text("System Path")
        midThreeBox.pack_start(nameEntry, True, True, 10)

        self.browse2 = Gtk.Button(label="Browse")
        self.browse2.connect("clicked", self.browse2_clicked)
        midThreeBox.pack_start(self.browse2, True, True, 10)

        self.generate = Gtk.Button(label="Generate")
        self.generate.connect("clicked", self.generate_clicked)
        botBox.pack_start(self.generate, True, True, 10)

        self.cancel = Gtk.Button(label="Cancel")
        self.cancel.connect("clicked", self.cancel_clicked)
        botBox.pack_start(self.cancel, True, True, 10)

    def browse_clicked(self,widget):
        print("Browsing n shit")
    
    def browse2_clicked(self,widget):
        print("Browsing n shit")
    
    def generate_clicked(self,widget):
        print("Browsing n shit")
        self.destroy()
    
    def cancel_clicked(self,widget):
        print("Browsing n shit")
        self.destroy()
    
    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())



