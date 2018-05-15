class protocol_manager():
    
    protocolName = ""
    protocolAttbs = {}
    field = ""

    def __init__(self):
        self.protocolName = "new_protocol"
        self.protocolAttbs['protoName'] = self.protocolName
        self.field = "zewardo"
        self.protocolAttbs['field'] = self.field

    def __init__(self, name):
        self.protocolName = name
        self.protocolAttbs['protoName'] = self.protocolName
        self.field = ( name + "montez" ) 
        self.protocolAttbs['field'] = self.field

    def generate_intermediate_script():
        pass

if __name__ == '__main__':
    PM = protocol_manager( "lola" )
    print PM.protocolAttbs
    print PM.protocolAttbs[ 'protoName' ]
    print "the end!"