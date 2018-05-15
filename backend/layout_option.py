import Tkinter as tk
import tkFileDialog
#import AppKit

#Will list the layout options for the current project

class layout_options():
    def __init__(self):
        print('In layout option class')

    def project_options(self):
        print("In project option def in the layout option class")

    def store_layoutoption_fields(self, view, xcor, ycor, width, height):
        self.file = open("workspaceInfo.txt", "w")
        #self.file.write("Hello WOrld")
        with open("layoutFields.txt", "w") as write:
            write.write("View=" +view+"\n")
            write.write("X_Coordinate="+xcor)
            write.write("Y_Coordinate=" + ycor)
            write.write("Width=" + width)
            write.write("Height=" + height)

#Contracts: Gives options for project
#Contracts: Gives options for workspace
        
