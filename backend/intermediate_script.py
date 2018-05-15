import xml.etree.ElementTree as ET

from protocol_decision_tree import ProtocolDecisionTree

class IntermediateScript:

    def __init__(self):
        self.PDT_list = []

    def getPDTList(self):
        return self.PDT_list

    def insertToPDTList(self, PDTNode):
        currentNode = PDTNode
        self.PDT_list.insert(len(self.PDT_list), currentNode.encapsulate())

    def PDTtoList(self, tree):
        self.PDT_list = []
        currentNode = tree.PDT
        self.insertToPDTList(currentNode)
        while currentNode.getNext():
            currentNode = currentNode.getNext()
            self.insertToPDTList(currentNode)

    def PDTtoXML(self, tree):
        self.PDTtoList(tree)
        root = ET.Element('Protocol Decision Tree')
        for i in self.PDT_list:
            currComp = ET.SubElement(root, 'Component ID')
            currType = ET.SubElement(currComp, 'Type')
            currNext = ET.SubElement(currComp, 'Next')

            currComp.text = self.PDT_list[self.PDT_list.index(i)][0]
            currType.text = self.PDT_list[self.PDT_list.index(i)][1]
            currNext.text = str(self.PDT_list[self.PDT_list.index(i)][2])

            if self.PDT_list[self.PDT_list.index(i)][1] == 'field':
                currNAME = ET.SubElement(currComp, 'NAME')
                currABBREV = ET.SubElement(currComp, 'ABBREV')
                currDESCRIPTION = ET.SubElement(currComp, 'DESCRIPTION')
                currREFERENCELIST = ET.SubElement(currComp, 'REFERENCELIST')
                currDATATYPE = ET.SubElement(currComp, 'DATATYPE')
                currBASE = ET.SubElement(currComp, 'BASE')
                currMASK = ET.SubElement(currComp, 'MASK')
                currVALUECONSTR = ET.SubElement(currComp, 'VALUECONSTR')
                currREQUIRED = ET.SubElement(currComp, 'REQUIRED')

                currNAME.text = str(self.PDT_list[self.PDT_list.index(i)][3])
                currABBREV.text = str(self.PDT_list[self.PDT_list.index(i)][4])
                currDESCRIPTION.text = str(self.PDT_list[self.PDT_list.index(i)][5])
                currREFERENCELIST.text = str(self.PDT_list[self.PDT_list.index(i)][6])
                currDATATYPE.text = str(self.PDT_list[self.PDT_list.index(i)][7])
                currBASE.text = str(self.PDT_list[self.PDT_list.index(i)][8])
                currMASK.text = str(self.PDT_list[self.PDT_list.index(i)][9])
                currVALUECONSTR.text = str(self.PDT_list[self.PDT_list.index(i)][10])
                currREQUIRED.text = str(self.PDT_list[self.PDT_list.index(i)][11])

            if self.PDT_list[self.PDT_list.index(i)][1] == 'start_field':
                currPROTOCOLNAME = ET.SubElement(currComp, 'PROTOCOLNAME')
                currPROTOCOLDESCR = ET.SubElement(currComp, 'PROTOCOLDESCR')
                currDEPENDENTPROTONAME = ET.SubElement(currComp, 'DEPENDENTPROTONAME')
                currDEPENDENCYPATTERN = ET.SubElement(currComp, 'DEPENDENCYPATTERN')

                currPROTOCOLNAME.text = str(self.PDT_list[self.PDT_list.index(i)][3])
                currPROTOCOLDESCR.text = str(self.PDT_list[self.PDT_list.index(i)][4])
                currDEPENDENTPROTONAME.text = str(self.PDT_list[self.PDT_list.index(i)][5])
                currDEPENDENCYPATTERN.text = str(self.PDT_list[self.PDT_list.index(i)][6])

            if self.PDT_list[self.PDT_list.index(i)][1] == 'reference_list':
                currREFERENCELISTNAME = ET.SubElement(currComp, 'REFERENCELISTNAME')
                currREFERENCELIST = ET.SubElement(currComp, 'REFERENCELIST')

                currREFERENCELISTNAME.text = str(self.PDT_list[self.PDT_list.index(i)][3])
                currREFERENCELIST.text = str(self.PDT_list[self.PDT_list.index(i)][4])

            if self.PDT_list[self.PDT_list.index(i)][1] == 'packet_info_list':
                currPACKETINFOLIST = ET.SubElement(currComp, 'PACKETINFOLIST')

                currPACKETINFOLIST.text = str(self.PDT_list[self.PDT_list.index(i)][3])

        #ET.dump(root)
        return root

    def XMLtoPDT(self, tree):
        pass

if __name__ == '__main__':
    #pass
    tree = ProtocolDecisionTree()
    print str(tree)

    IS = IntermediateScript()
    IS.PDTtoList(tree)

    print str(IS.PDT_list)

    tree.addStartField()
    tree.addField()
    tree.addEndField()

    print str(tree)

    IS.PDTtoList(tree)

    print str(IS.PDT_list)

    ET.dump(IS.PDTtoXML(tree))