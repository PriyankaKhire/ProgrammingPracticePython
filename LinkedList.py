#Linked list

class Node:
    def __init__(self):
        self.data = None
        self.link = None

    def getData(self):
        return self.data

    def getLink(self):
        return self.link

    def setData(self, data):
        self.data = data

    def setLink(self, link):
        self.link = link


#Main Program
newNode = Node()
newNode.setData(10)
newNode1 = Node()
newNode1.setData(20)
newNode.setLink(newNode1)
print newNode1.getData()
print newNode.getLink()
#just like in c++ you used -> operator and here you are using . operator
print newNode.getLink().getData()
