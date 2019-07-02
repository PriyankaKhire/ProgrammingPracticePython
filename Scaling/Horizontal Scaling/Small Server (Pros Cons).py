#Horizontal Scalling
import sys
sys.path.append("../..")
from ColorText import ColorText

print "Pros and cons of horizontal scalling versus vertical scalling"

ct = ColorText()
ct.display('We horizontal scale by adding several small servers/machines.', 'brown')
ct.display('We need a load balencer here', 'light-red')
ct.display('If one of the machine fails, you can redirect the request to the several other machines', 'green')
ct.display('What ever communication we have between the machines, it is over the network, and networks are usually slow as comapred to inter-process communication', 'light-red')
ct.display('Data can be inconsistant, because there are several machines, it may take some time for machines to copy data from other machines', 'light-red')
ct.display('Scales well, we can add as many servers/machines as we like', 'green')
