from component import Component

class PacketInformation(Component):

    def __init__(self, ID):
        Component.__init__(self, ID, 'packet_info_list', None)
        self.PACKETINFOLIST = {}

    def setPACKETINFOLIST(self, PIList):
        self.PACKETINFOLIST = PIList

    def getPACKETINFOLIST(self):
        return self.PACKETINFOLIST

    def addPacketInfoElement(self, key, value):
        if key in self.PACKETINFOLIST:
            print "Error: Item already in Packet Info List"
        else:
            self.PACKETINFOLIST[key] = value

    def editPacketInfoElement(self, key, value):
        if key in self.PACKETINFOLIST:
            self.PACKETINFOLIST[key] = value
        else:
            print "Error: Key not found"

    def delPacketInfoElement(self, key):
        del(self.PACKETINFOLIST[key])

    def encapsulate(self):
        return [self.FieldID, self.FieldType, self.NextField,
                self.PACKETINFOLIST]

    def detailedStr(self):
        currField = '(' + str(self.FieldID) + ':' + str(self.FieldType) + ':' + str(self.PACKETINFOLIST)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + str(nextID) + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass