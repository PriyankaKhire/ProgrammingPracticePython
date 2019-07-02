#Vertical Scaling
import sys
sys.path.append("../..")
from ColorText import ColorText

ct = ColorText()
ct.display("We vertical scale by adding more power to our existing server", "brown")
ct.display("We can increase power of our existing machine by adding more processing power, giving it more storage, etc.", "brown")
ct.display("We dont require a load balancer since there is just one big system", "green")
ct.display("But if this one big system fails then the entire service goes down", "light-red")
ct.display("If we want to communicate between 2 independent systems, then we have inter process communication thats faster.", "green")
ct.display("The data just resides on one system, so data will always be consistent", "green")
ct.display("There will eventually be some hardware limitaitons, so it eventually won't scale", "light-red")
