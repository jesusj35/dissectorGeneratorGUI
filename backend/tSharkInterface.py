"""
@author Jesus Juarez
@Description This class serves as the t shark interface with the protocol dissector generator.
             Changes LUA to PDML and PSML
"""
import os

class tSharkInterface:
    
    def getInfo(self, packet, scriptName):
        self.p = packet;

        if self.p is None:
            print "Error: Packet is empty"
        else:

            command = "tshark -T pdml -X lua_script:" + scriptName + " -r " + self.p + " -V > dissection"
            os.system(command)

            command = "tshark -T psml -X lua_script:" + scriptName + " -r " + self.p + " -V > dissection"
            os.system(command)

 
    

            