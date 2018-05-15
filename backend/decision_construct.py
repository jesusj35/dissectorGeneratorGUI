from component import Component

class DecisionConstruct:

    def __init__(self, expressions, connectors):
        Component.__init__(self, ID, 'expression', None)
        self.EXPRESSIONS = expressions
        self.CONNECTORS = connectors