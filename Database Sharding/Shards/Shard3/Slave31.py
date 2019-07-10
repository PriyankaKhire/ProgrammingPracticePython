#Slave
import sys
import os.path
sys.path.append("../../HelperFunctions")
from SlaveServer import SlaveServer

class Slave31(object):
    def __init__(self):
        slave = SlaveServer('Slave31', 'Master3')
        slave.run()

#Main
obj = Slave31()
        
        
