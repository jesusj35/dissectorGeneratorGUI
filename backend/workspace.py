import Tkinter as tk
import tkFileDialog
#import AppKit

#Area where analyst will be able to work with various components of a porject and work with them as a cohesive unit.

class workspace():
    def __init__(self):
        print("in write workspace file")
        self.workspace_name = []
        self.workspace_path = {}

    def write_workspace_data_file(self, directory, dirName):
        self.file = open("workspaceInfo.txt", "w")
        #self.file.write("Hello WOrld")
        with open("workspaceInfo.txt", "w") as write:
            write.write("Name=" +dirName+"\n")
            write.write("Path="+directory)

    def export_to_lua(self):
        print("This is the file that will be exported as a LUA file")



#       self.file.close()


if __name__ == '__main__':
    root = tk.Tk()
    app = workspace(root)
    # AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    # app.mainloop()






#Contract: Export Dissector

#Contract: Display/store customizable work area"""


    
