#Stack Min
#Design stack that returns min element of the stack in O(1)

stack = []
minStack = []

def pop():
    global stack, minStack
    if not stack:
        print "stack empty"
        return
    print "Popped element is "+str(stack[-1])
    if(stack[-1] == minStack[-1]):
        del minStack[-1]
    del stack[-1]

def push():
    data = raw_input("Enter data ")
    data = int(data)
    global stack, minStack
    stack.append(data)
    if not minStack:
        minStack.append(data)
    else:
        if(minStack[-1] > data):
            minStack.append(data)

def getMin():
    global stack, minStack
    print "Min element in the stack is "+str(minStack[-1])

def displayStacks():
    global stack, minStack
    print "Stack "+str(stack)
    print "Min Stack "+str(minStack)

#Main Program
options = {
    0 : push,
    1 : pop,
    2 : getMin,
    3 : displayStacks
    }
ch = True
while(ch):
    ch = raw_input("Enter choice : \n 0 -> push\n1 -> pop\n2 -> GetMin\n3 -> display\n")
    options[int(ch)]()
    ch = raw_input("Do you wish to continue ? y/n \n")
    if(ch == 'y'):
        ch = True
    else:
        ch = False
    
