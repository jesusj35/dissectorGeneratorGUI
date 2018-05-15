from component import Component

class EndField(Component):

    def __init__(self, ID):
        Component.__init__(self, ID, 'end_field', None)

    def encapsulate(self):
        return [self.FieldID, self.FieldType, self.NextField]

    def detailedStr(self):
        currField = '(' + str(self.FieldID) + ':' + str(self.FieldType)

        if self.NextField:
            nextID = str(self.NextField.FieldID)
            currField += ':' + str(nextID) + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass