from component import Component

class Field(Component):

    def __init__(self, ID, name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required):
        Component.__init__(self, ID, 'field', None)
        self.NAME = name
        self.ABBREV = abbrev
        self.DESCRIPTION = descr
        self.REFERENCELIST = referencelist
        self.DATATYPE = datatype
        self.BASE = base
        self.MASK = mask
        self.VALUECONSTR = valueconstr
        self.REQUIRED = True

    def setNAME(self, name):
        self.NAME = name

    def setNAME(self):
        return self.NAME

    def serABBREVs(self, abbrev):
        self.ABBREV = abbrev

    def gerABBREVs(self):
        return self.ABBREV

    def setDESCRIPTION(self, descr):
        self.DESCRIPTION = descr

    def getDESCRIPTION(self):
        return self.DESCRIPTION

    def setREFERENCELIST(self, referencelist):
        self.REFERENCELIST = referencelist

    def getREFERENCELIST(self):
        return self.REFERENCELIST

    def setDATATYPE(self, datatype):
        self.DATATYPE = datatype

    def getDATATYPE(self):
        return self.DATATYPE

    def setBASE(self, base):
        self.BASE = base

    def getBASE(self):
        return self.BASE

    def setMASK(self, mask):
        self.MASK = mask

    def getMASK(self):
        return self.MASK

    def setVALUECONSTR(self, valueconstr):
        self.VALUECONSTR = valueconstr

    def getVALUECONSTR(self):
        return self.VALUECONSTR

    def setREQUIRED(self, value):
        self.REQUIRED = value

    def getREQUIRED(self):
        return self.REQUIRED

    def encapsulate(self):
        return [self.FieldID, self.FieldType, self.NextField,
                self.NAME, self.ABBREV, self.DESCRIPTION, self.REFERENCELIST,
                self.DATATYPE, self.BASE, self.MASK, self.VALUECONSTR, self.REQUIRED]

    def detailedStr(self):
        currField = '(' + str(self.FieldID) + ':'+ str(self.FieldType) + \
                    ':' + str(self.NAME) + ':' + str(self.ABBREV) + \
                    ':' + str(self.DESCRIPTION) + '":' + str(self.REFERENCELIST) + \
                    ':' + str(self.DATATYPE) + ':' + str(self.BASE) + \
                    ':' + str(self.MASK) + ':' + str(self.VALUECONSTR) + \
                    ':' + str(self.REQUIRED)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + str(nextID) + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    #newField = Field('newField', 'nf', 'a new field', 'None', 'int', '8', 'None', 'None', '0')
    #print newField.getField()
    pass