#Slave
import sys
import os.path
sys.path.append("../../HelperFunctions")
from SlaveServer import SlaveServer

class Slave22(object):
    def __init__(self):
        slave = SlaveServer('Slave22', 'Master2')
        slave.run()

#Main
obj = Slave22()
        
        
