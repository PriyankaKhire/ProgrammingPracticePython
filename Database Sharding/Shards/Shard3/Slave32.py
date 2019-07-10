#Slave
import sys
import os.path
sys.path.append("../../HelperFunctions")
from SlaveServer import SlaveServer

class Slave32(object):
    def __init__(self):
        slave = SlaveServer('Slave32', 'Master3')
        slave.run()

#Main
obj = Slave32()
        
        
