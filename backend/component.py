class Component:

    def __init__(self, fID, ftype, nextField):
        self.FieldID = fID
        self.FieldType = ftype
        self.NextField = nextField

    def setFieldID(self, fID):
        self.FieldID = fID

    def getFieldID(self):
        return self.FieldID

    def setType(self, ftype):
        self.FieldType = ftype

    def getType(self):
        return self.FieldType

    def getNext(self):
        return self.NextField

    def setNext(self, nextField):
        self.NextField = nextField

    def encapsulate(self):
        return [self.FieldID, self.FieldType, self.NextField]

    def detailedStr(self):
        return str(self)

    def __str__(self):
        component = '(' + str(self.FieldID) + ':' + str(self.FieldType)
        if self.NextField:
            nextID = self.NextField.FieldID
            component += ':' + str(nextID) + ')'
        else:
            component += ':None)'
        return component

if __name__ == '__main__':
    pass