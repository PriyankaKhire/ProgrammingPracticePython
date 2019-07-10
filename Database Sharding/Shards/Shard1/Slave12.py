#Slave
import sys
import os.path
sys.path.append("../../HelperFunctions")
from SlaveServer import SlaveServer

class Slave12(object):
    def __init__(self):
        slave = SlaveServer('Slave12', 'Master1')
        slave.run()

#Main
obj = Slave12()
        
        
