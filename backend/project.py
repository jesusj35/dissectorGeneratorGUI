import Tkinter as tk
import tkFileDialog


# import AppKit

# Information provided to the analyst on the project, if available....

# Provide project description, which will be stored in a file
class project:
    def __init__(self):
        print("in read file(project)")
        self.project_names = []
        self.project_descriptions = {}

    def read_project_data_file(self):
        self.file = open("Projects.txt", "r")
        for line in self.file:
            if line.startswith("Name="):
                self.project_names.append(line[5:])
            #if line.startswith("Description="):
                #print(line[12:])
                #self.project_descriptions
        self.file.close()

    def save_project_data_file(self,name,description):
        file_data = ""
        file_r = open("Projects.txt", "r")

        for line in file_r:
            file_data = file_data + line

        print(file_data)
        file_r.close()

        file_w = open("Projects.txt", "w")

        with file_w as write:
            if len(file_data) != 0:
                write.write(file_data+"\n")

            write.write("Name=" + name + "\n")
            write.write("Description=" + description)

        file_w.close()

    def create_project_on_project_nav(self):
        print()

if __name__ == '__main__':
    root = tk.Tk()
    app = project(root)
    # AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    # app.mainloop()
