'''@author Jesus Juarez 
   @description File holding all output areas'''
import Tkinter as tk
import packetStream as ps
import dissectedStream as ds
import rawData as raw
import console as console

import ttk

class OutputView(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
       
        #Create notebook
        notebook = ttk.Notebook(self.master,width=200, height=100)
        notebook.pack()

        #Tabs
        packet_stream_tab = ps.packetStream(notebook)
        notebook.add(packet_stream_tab, text="Packet Stream Area")

        
        dissected_stream_tab = ds.dissecteStream(notebook)
        notebook.add(dissected_stream_tab, text="Dissected Stream Area")

        
        raw_data_tab = raw.rawData(notebook)
        notebook.add(raw_data_tab, text="Raw Data Area")

      
        console_area_tab = console.console(notebook)
        notebook.add(console_area_tab, text="Console Area")

if __name__ == '__main__':
    root = tk.Tk()
    OutputView = OutputView(root)
    OutputView.mainloop()