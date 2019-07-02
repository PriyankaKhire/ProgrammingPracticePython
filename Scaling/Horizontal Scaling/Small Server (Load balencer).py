#Horizontal Scalling
import sys
sys.path.append("../..")
from ColorText import ColorText

print "Operations of load balencers"

ct = ColorText()
ct.display('Each of these small machine is running a copy of your program.', 'brown')
ct.display('Our load balencer is responsible for distributing the load evenly amongst all these small machines', 'green')
ct.display('Load balencer also pings the machine to check if it is up and running or not', 'brown')
