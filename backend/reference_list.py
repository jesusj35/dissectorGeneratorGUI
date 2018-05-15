from component import Component

class ReferenceList(Component):

    def __init__(self, ID, reflistname):
        Component.__init__(self, ID, 'reference_list', None)
        self.REFERENCELISTNAME = reflistname
        self.REFERENCELIST = {}

    def setREFERENCELISTNAME(self, rlname):
        self.REFERENCELISTNAME = rlname

    def getREFERENCELISTNAME(self):
        return self.REFERENCELISTNAME

    def setREFERENCELIST(self, reflist):
        self.REFERENCELIST = reflist

    def getREFERENCELIST(self):
        return self.REFERENCELIST

    def addReferenceElement(self, key, value):
        if key in self.REFERENCELIST:
            print "Error: Item already in Reference List"
        else:
            self.REFERENCELIST[key] = value

    def editReferenceElement(self, key, value):
        if key in self.REFERENCELIST:
            self.REFERENCELIST[key] = value
        else:
            print "Error: Key not found"

    def delReferenceElement(self, key):
        del(self.REFERENCELIST[key])

    def encapsulate(self):
        return [self.FieldID, self.FieldType, self.NextField,
                self.REFERENCELISTNAME, self.REFERENCELIST]

    def detailedStr(self):
        currField = '(' + str(self.FieldID) + ':' + str(self.FieldType) + ':' + \
                    str(self.REFERENCELISTNAME) + ':' + str(self.REFERENCELIST)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + str(nextID) + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass