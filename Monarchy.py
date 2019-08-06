#Monarchy
#https://leetcode.com/discuss/interview-question/302164/Google-or-Phone-Screen-or-Monarchy
class Monarch(object):
    def __init__(self):
        self.name = None
        self.childern = []
        self.isAlive = True
        
class Monarchy(object):
    def __init__(self):
        self.firstMonarch = None
        self.monarchs = {}
        
    def birth(self, child, parent):
        # create monarch
        monarch = Monarch()
        monarch.name = child
        # If it's the first monarch
        if(parent == None and self.firstMonarch == None):
            self.firstMonarch = monarch
        else:
            # find parent and add child
            if not (parent in self.monarchs):
                print "Parent not found"
                return
            self.monarchs[parent].childern.append(monarch)
        # Add the monarch to hash table
        self.monarchs[child] = monarch

    def death(self, name):
        # I don't understand the purpose of this function
        self.monarchs[name].isAlive = False

    def preOrder(self, node):
        if(node):
            print node.name
            for child in node.childern:
                self.preOrder(child)

    def getOrderOfSuccession(self):
        self.preOrder(self.firstMonarch)

# Main
m = Monarchy()
m.birth("king", None)
m.birth("Andy", "king")
m.birth("Bob", "king")
m.birth("Catherine", "king")
m.birth("Matthew" , "Andy")
m.birth("Alex " , "Bob")
m.birth("Asha " , "Bob")
m.getOrderOfSuccession()
