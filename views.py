import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 

class Views(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Export")

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(mainBox)

        topBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        topBox.set_homogeneous(False)

        top2Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        top2Box.set_homogeneous(False)

        botBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        botBox.set_homogeneous(False)
        
        holdBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        holdBox.set_homogeneous(False)

        leftBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        leftBox.set_homogeneous(False)

        midBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        midBox.set_homogeneous(False)

        rightBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        rightBox.set_homogeneous(False)

        holdBox.pack_start(leftBox, True, True, 10)
        holdBox.pack_start(midBox, True, True, 10)
        holdBox.pack_start(rightBox, True, True, 10)

        mainBox.pack_start(topBox, True, True, 10)
        mainBox.pack_start(top2Box, True, True, 10)
        mainBox.pack_start(holdBox, True, True, 10)
        mainBox.pack_start(botBox, True, True, 10)


        label = Gtk.Label("Customize the views.")
        label.set_justify(Gtk.Justification.CENTER)
        topBox.pack_start(label, True, True, 10)
        
        shoLabel = Gtk.Label("                                      ")
        shoLabel.set_justify(Gtk.Justification.CENTER)
        top2Box.pack_start(shoLabel, True, True, 10)

        hideLabel = Gtk.Label("Hide")
        hideLabel.set_justify(Gtk.Justification.CENTER)
        top2Box.pack_start(hideLabel, True, True, 10)

        showLabel = Gtk.Label("Show")
        showLabel.set_justify(Gtk.Justification.CENTER)
        top2Box.pack_start(showLabel, True, True, 10)

        
        #Project Navigation 
        navigationLabel = Gtk.Label("Project Navigation")
        navigationLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(navigationLabel, True, True, 10)
        
        projectHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        projectHide.connect("toggled", self.on_button_toggled_project, "1")
        midBox.pack_start(projectHide, False, False, 10)

        projectShow = Gtk.RadioButton.new_from_widget(projectHide)
        projectShow.connect("toggled", self.on_button_toggled_project, "2")
        rightBox.pack_start(projectShow, False, False, 12)
        
        #Dissector Builder Area
        buildLabel = Gtk.Label("Dissector Build Area")
        buildLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(buildLabel, True, True, 10)

    
        buildHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        buildHide.connect("toggled", self.on_button_toggled_build, "1")
        midBox.pack_start(buildHide, False, False, 10)

        buildShow = Gtk.RadioButton.new_from_widget(buildHide)
        buildShow.connect("toggled", self.on_button_toggled_build, "2")
        rightBox.pack_start(buildShow, False, False, 12)

              
        #Palettee Area
        paletteLabel = Gtk.Label("Palette")
        paletteLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(paletteLabel, True, True, 10)

        paletteHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        paletteHide.connect("toggled", self.on_button_toggled_palette, "1")
        midBox.pack_start(paletteHide, False, False, 10)

        paletteShow = Gtk.RadioButton.new_from_widget(paletteHide)
        paletteShow.connect("toggled", self.on_button_toggled_palette, "2")
        rightBox.pack_start(paletteShow, False, False, 13)

        
        #Packet Stream Area
        streamLabel = Gtk.Label("Packet Stream Area")
        streamLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(streamLabel, True, True, 10)

        packetStreamHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        packetStreamHide.connect("toggled", self.on_button_toggled_build, "1")
        midBox.pack_start(packetStreamHide, False, False, 10)

        packetStreamShow = Gtk.RadioButton.new_from_widget(packetStreamHide)
        packetStreamShow.connect("toggled", self.on_button_toggled_packet, "2")
        rightBox.pack_start(packetStreamShow, False, False, 13)

        
        #Dissected Stream Area
        dissectedLabel = Gtk.Label("Dissected Stream Area")
        dissectedLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(dissectedLabel, True, True, 10)

        dissectedStreamHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        dissectedStreamHide.connect("toggled", self.on_button_toggled_build, "1")
        midBox.pack_start(dissectedStreamHide, False, False, 10)

        dissectedStreamShow = Gtk.RadioButton.new_from_widget(dissectedStreamHide)
        dissectedStreamShow.connect("toggled", self.on_button_toggled_dissected, "2")
        rightBox.pack_start(dissectedStreamShow, False, False, 13)


        #Raw Label Area
        rawLabel = Gtk.Label("Raw Data Area")
        rawLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(rawLabel, True, True, 10)

        rawHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        rawHide.connect("toggled", self.on_button_toggled_build, "1")
        midBox.pack_start(rawHide, False, False, 10)

        rawShow = Gtk.RadioButton.new_from_widget(rawHide)
        rawShow.connect("toggled", self.on_button_toggled_raw, "2")
        rightBox.pack_start(rawShow, False, False, 12)

        
        #Console Label Area
        consoleLabel = Gtk.Label("Console Area")
        consoleLabel.set_justify(Gtk.Justification.CENTER)
        leftBox.pack_start(consoleLabel, True, True, 10)

        consoleHide = Gtk.RadioButton.new_with_label_from_widget(None, "")
        consoleHide.connect("toggled", self.on_button_toggled_build, "1")
        midBox.pack_start(consoleHide, False, False, 10)

        consoleShow = Gtk.RadioButton.new_from_widget(consoleHide)
        consoleShow.connect("toggled", self.on_button_toggled_console, "2")
        rightBox.pack_start(consoleShow, False, False, 12)

        #Buttons 
        restoreButton = Gtk.Button.new_with_label("Restore to Default")
        restoreButton.connect("clicked", self.restore_clicked, projectShow, buildShow, paletteShow, packetStreamShow,
        dissectedStreamShow, rawShow, consoleShow)
        botBox.pack_start(restoreButton, False, False, 5)

        confirmButton = Gtk.Button.new_with_label("Confirm")
        confirmButton.connect("clicked", self.confirm_clicked)
        botBox.pack_start(confirmButton, False, False, 5)

        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        botBox.pack_start(cancelButton, False, False, 5)

        
    def on_button_toggled_project(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def on_button_toggled_build(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)
    
    def on_button_toggled_palette(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)  

    def on_button_toggled_packet(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)   
    
    def on_button_toggled_dissected(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state) 
    
    def on_button_toggled_raw(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state) 
    
    def on_button_toggled_console(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state) 
    
    def restore_clicked(self,button, projectShow, buildShow, paletteShow, packetStreamShow,
        dissectedStreamShow, rawShow, consoleShow):
        print("Browse")
        projectShow.set_active(True)
        buildShow.set_active(True)
        paletteShow.set_active(True)
        packetStreamShow.set_active(True)
        dissectedStreamShow.set_active(True)
        rawShow.set_active(True)
        consoleShow.set_active(True)

    def confirm_clicked(self,widget):
        print("Confirm")
        self.destroy()

    def cancel_clicked(self,widget):
        print("Cancel")
        self.destroy()

