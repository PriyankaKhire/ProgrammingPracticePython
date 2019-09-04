'''
Given a list of lists, implement an iterator class to allow the client to traverse
and remove elements in the list.
This iterator should provide three public class member functions:
/**
* Return true or false if there is another element in the set.
*/
public boolean hasNext();

/**
* Return the value of the next element in the set.
*/
public int next();

/**
* Remove the last element returned by the iterator. That is, remove the element that the previous 'next()' returned.
* This method can be called only once per call to next(), otherwise, an exception will be thrown.
* See http://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html#remove() for details.
*/
public void remove();

The code should be well structured, and robust enough to handle any access pattern.
Additionally, write code to demonstrate that the class can be used for the following basic scenarios:

Print elements

Given: [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
Print: 1 2 3 4 5 6 7 8 9 10

Remove even elements

Given: [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
Should result in: [[],[1,3],[5],[],[],[],[7],[],[9],[],[]]
Print: 1 3 5 7 9

### Should be done in place without constructing any additional lists ###
(otherwise you can just flatten the list)
'''
class Iterator(object):
    def __init__(self, s):
        self.set = s
        #self.flatten()
        self.ptr = None
        self.currentSetIndex = None
        self.setInitialPtr()
        self.prevNext = None
        self.eol = False

    def setInitialPtr(self):
        for i in range(len(self.set)):
            if(self.set[i]):
                self.currentSetIndex = i
                self.ptr = 0
                return

    # Should be done in place.
    '''
    def flatten(self):
        newSet = []
        for l in self.set:
            if(l):
                newSet = newSet+l
        self.set = newSet[:]
    '''

    def hasNext(self):
        for l in self.set:
            if(l):
                return True
        return False

    def Next(self):
        if(not(self.hasNext()) or self.eol):
            print "Reached end of list"
            self.prevNext = None
            return
        print "Currently on ->",self.set[self.currentSetIndex][self.ptr]
        self.prevNext = [self.currentSetIndex, self.ptr]
        self.incrementPtr()

    def incrementPtr(self):
        if(self.ptr < len(self.set[self.currentSetIndex])-1):
            self.ptr = self.ptr + 1
        else:
            for i in range(self.currentSetIndex+1, len(self.set)):
                if(self.set[i]):
                    self.currentSetIndex = i
                    self.ptr = 0
                    return
            self.eol = True

    def decrementPtr(self):
        if not(self.hasNext()):
            print "Set empty"
            return
        if(self.ptr > 0):
            self.ptr = self.ptr - 1

    def remove(self):
        if(self.prevNext):
            print "Removed ->",self.set[self.prevNext[0]].pop(self.prevNext[1])
            self.decrementPtr()
        else:
            print "Exception"
        self.prevNext = None
        print self.set

# Main
obj = Iterator([[], [], [], []])
print obj.hasNext()
print "*"*30
obj = Iterator([[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]])
print obj.hasNext()
obj.Next()
obj.remove()
obj.Next()     
obj.remove()
obj.Next()     
obj.remove()
obj.remove()
obj.Next()
obj.remove()
obj.Next()     
obj.remove()
obj.Next()
obj.remove()
obj.Next()     
obj.remove()
obj.Next()
obj.remove()
obj.Next()     
obj.remove()
obj.remove()
obj.Next()     
obj.Next()
obj.remove()
obj.remove()
obj.remove()
obj.Next()
print obj.hasNext()
print "*"*30
obj = Iterator([[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]])
obj.Next()
obj.Next()
obj.remove()
obj.Next()
obj.Next()
obj.remove()
obj.Next()
obj.Next()
obj.remove()
obj.Next()
obj.Next()
obj.remove()
obj.Next()
obj.Next()
obj.remove()
obj.Next()
obj.Next()
obj.remove()
print "*"*30
obj = Iterator([[],[],[],[],[],[1]])
print obj.hasNext()
obj.Next()
obj.Next()
obj.remove()
print "*"*30
obj = Iterator([[],[],[],[],[],[1],[],[],[],[],[]])
obj.Next()
obj.Next()
obj.Next()
obj.remove()
print "*"*30
obj = Iterator([[],[],[],[],[],[1],[],[],[],[],[2]])
obj.Next()
obj.Next()
obj.remove()
obj.Next()
