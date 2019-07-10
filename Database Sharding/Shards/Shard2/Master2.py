#Master
import sys
sys.path.append("../../HelperFunctions")
from MasterServer import MasterServer

class Master2(object):
    def __init__(self):
        master = MasterServer('Master2')
        master.run(['Slave21', 'Slave22'])

#Main
obj = Master2()
        
