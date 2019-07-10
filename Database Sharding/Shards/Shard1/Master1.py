#Master
import sys
sys.path.append("../../HelperFunctions")
from MasterServer import MasterServer

class Master1(object):
    def __init__(self):
        master = MasterServer('Master1')
        master.run(['Slave11', 'Slave12'])

#Main
obj = Master1()
        
