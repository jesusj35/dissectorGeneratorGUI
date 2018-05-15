from component import Component

class DecisionConstruct:

    def __init__(self, result, previousField):
        Component.__init__(self, ID, 'expression', None)
        self.PreviousField = previousField
        self.EXPRESSIONRESULT = result