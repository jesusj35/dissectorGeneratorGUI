from component import Component
from field import Field
from start_field import StartField
from end_field import EndField
from reference_list import ReferenceList
from packet_information import PacketInformation

class ProtocolDecisionTree:

    def __init__(self, name = 'DEFAULT'):
        self.componentCount = 0

        root_ID = 'comp' + str(self.componentCount)
        self.PDT = Component(root_ID, 'root', None)
        self.PDT_Description = ""
        self.PDT_name = name

        self.PDT_end = self.PDT
        self.componentCount += 1

    def setPDTName(self, name):
        self.PDT_name = name

    def getPDTName(self):
        return self.PDT_name

    def getDescription(self):
        return self.PDT_Description

    def enterDescription(self, description):
        self.PDT_Description = '' + description

    def updatePDTEnd(self, object):
        self.PDT_end.NextField = object
        self.PDT_end = self.PDT_end.NextField
        self.componentCount += 1

    def deleteComponent(self, component):
        currentParent = self.PDT
        current = currentParent.getNext()
        while current:
            if str(current.FieldID) == str(component):
                currentParent.setNext(current.getNext())
                if currentParent.getNext() == None:
                    self.PDT_end = currentParent;
                return
            else:
                currentParent = current
                current = current.getNext()
        print "Error: Component does not exist in PDT"
        return

    def addField(self, name = 'DEFAULT', abbrev = 'DEFAULT', descr = 'DEFAULT', referencelist = None,
                 datatype = 'DEFAULT', base = 'DEFAULT', mask = 'DEFAULT', valueconstr = 'DEFAULT', required = False):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(Field(ID, name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required))

    def addStartField(self, protocolname = 'DEFAULT', protocoldescr = 'DEFAULT',
                      dependentprotoname = 'DEFAULT', dependencypattern = 'DEFAULT'):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(StartField(ID, protocolname, protocoldescr, dependentprotoname, dependencypattern))

    def addEndField(self):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(EndField(ID))

    def addReferenceList(self, reflistname = 'DEFAULT'):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(ReferenceList(ID, reflistname))

    def addPacketInfoList(self):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(PacketInformation(ID))

    def findComponent(self, component):
        current = self.PDT
        while current:
            if current.FieldID == component:
                return current
            current = current.NextField
        print "Error: component not in list"
        return None

    def detailedPDT(self):
        current = self.PDT
        PDT_str = 'Protocol Decission Tree: ' + self.getPDTName() + '. "' + self.getDescription() + '"\n' + '[' + current.detailedStr() + ' '
        current = current.NextField
        while current:
            PDT_str += current.detailedStr() + ' '
            current = current.NextField
        PDT_str += ']'
        return PDT_str

    def __str__(self):
        current = self.PDT
        PDT_str = '[' + str(current) + ' '
        current = current.NextField
        while current:
            PDT_str += str(current) + ' '
            current = current.NextField
        PDT_str += ']'
        return PDT_str

if __name__ == '__main__':
    pass

