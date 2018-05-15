from component import Component

class ExpressionConstruct:

    def __init__(self, operands, operators):
        Component.__init__(self, ID, 'expression', None)
        self.OPPERANDS = operands
        self.OPERATORS = operators