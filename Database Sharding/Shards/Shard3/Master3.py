#Master
import sys
sys.path.append("../../HelperFunctions")
from MasterServer import MasterServer

class Master3(object):
    def __init__(self):
        master = MasterServer('Master3')
        master.run(['Slave31', 'Slave32'])

#Main
obj = Master3()
        
