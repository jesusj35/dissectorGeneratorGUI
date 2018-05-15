import os
import dpkt

class pcap:

    def openPCAP(pcapName):
        pcapName = "test.pcap"
        file = open(pcapName."r")

        if ".pcap" not in file:
            print "Error: Not of type PCAP"
        if os.stat(file).st_size == 0
            print "The file is empty"
        pcap = dpkt.pcap.Reader(f)
        return pcap

    def pcapList(file):
        
