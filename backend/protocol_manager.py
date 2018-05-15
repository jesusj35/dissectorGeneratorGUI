from protocol_decision_tree import ProtocolDecisionTree
from intermediate_script import IntermediateScript
import xml.etree.ElementTree as ET

class ProtocolManager:

    def __init__(self):
        self.PDT = ProtocolDecisionTree()

    def getPDT(self):
        return self.PDT

    def setPDTName(self, name):
        self.PDT.setPDTName()

    def getPDTName(self):
        return self.PDT.PDT_name

    def setPDTDescription(self, description):
        self.PDT.enterDescription('' + description)

    def getPDTDescription(self):
        return self.PDT.getDescription()

    def deleteComponent(self, component):
        currentParent = self.PDT
        currentParent.deleteComponent(component)

    def addField(self, name = 'DEFAULT', abbrev = 'DFLT', descr = '', referencelist = None,
                 datatype = 'None', base = 'base.NONE', mask = 'None', valueconstr = 'None', required = False):
        self.PDT.addField(name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required)

    def addStartField(self, protocolname = 'DEFAULT', protocoldescr = '',
                      dependentprotoname = '', dependencypattern = ''):
        self.PDT.addStartField(protocolname, protocoldescr, dependentprotoname, dependencypattern)

    def addEndField(self):
        self.PDT.addEndField()

    def addReferenceList(self, reflistname = 'DEFAULT'):
        self.PDT.addReferenceList(reflistname)

    def addPacketInfoList(self):
        self.PDT.addPacketInfoList()

    def findComponent(self, component):
        return self.PDT.findComponent(component)

    def generateIntermediateScript(self):
        IS = IntermediateScript()
        return IS.PDTtoXML(self.PDT)

if __name__ == '__main__':
    pass
    # test = ProtocolManager()
    # print str(test.PDT)
    # test.setPDTDescription("test pdt")
    # print test.getPDTDescription()
    # test.addStartField()
    # print str(test.PDT)
    # test.addField()
    # print str(test.PDT)
    # test.addPacketInfoList()
    # print str(test.PDT)
    # test.addReferenceList()
    # print str(test.PDT)
    # test.addEndField()
    # print str(test.PDT)
    # print str(test.PDT.detailedPDT())
    #
    # ET.dump(test.generateIntermediateScript())