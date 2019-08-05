#My Calendar II
#https://leetcode.com/problems/my-calendar-ii/
class MyCalendarTwoSolution1(object):
    #This solution does not work for all cases
    def __init__(self):
        self.hashTable = {}

    def addKeyToHash(self, key):
        if not(key in self.hashTable):
            self.hashTable[key] = 1
        else:
            self.hashTable[key] = self.hashTable[key] + 1

    def addBooking(self, startIndex, endIndex, sortedHashKeys, start, end):
        #Update all entries in betwen start and end
        while(startIndex < endIndex):
            self.hashTable[sortedHashKeys[startIndex]] = self.hashTable[sortedHashKeys[startIndex]] + 1
            startIndex = startIndex + 1
        #Add start and end to hash table
        self.addKeyToHash(start)
        self.addKeyToHash(end)
        

    def findTrippleBookings(self, startIndex, endIndex, sortedHashKeys):
        while(startIndex < endIndex):
            if(self.hashTable[sortedHashKeys[startIndex]] >= 2):
                return True
            startIndex = startIndex + 1
        return False

    def findElementsBetweenStartAndEnd(self, start, end, sortedHashKeys):
        for i in range(len(sortedHashKeys)):
            if(sortedHashKeys[i] > start):
                break
        for j in range(i, len(sortedHashKeys)):
            if(sortedHashKeys[j] > end):
                break
        print i, j, sortedHashKeys
        return i, j

    def insertInHash(self, start, end):
        if not self.hashTable:
            self.hashTable[start] = 1
            self.hashTable[end] = 1
            return True
        sortedHashKeys = sorted(self.hashTable)
        #Find indices between start and end
        startIndex, endIndex = self.findElementsBetweenStartAndEnd(start, end, sortedHashKeys)
        #Find if there are 3 bookings
        if(self.findTrippleBookings(startIndex, endIndex, sortedHashKeys)):
            return False
        #Add the booking
        self.addBooking(startIndex, endIndex, sortedHashKeys, start, end)
        return True

    def book(self, start, end):
        print self.insertInHash(start, end)
        print self.hashTable
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

class MyCalendarTwo(object):

    def __init__(self):
        self.hashTable = {}

    def insertStartEndInHash(self, start, end, startAdder, endAdder):
        #Insert start
        if not(start in self.hashTable):
            self.hashTable[start] = 1 + startAdder
        else:
            self.hashTable[start] = self.hashTable[start] + 1 + startAdder
        #Insert end
        if not(end in self.hashTable):
            self.hashTable[end] = -1 + endAdder
        else:
            self.hashTable[end] = self.hashTable[end] - 1 + endAdder

    def findTrippleBookingsBetweenStartAndEnd(self, start, end, sortedKeys):
        print "keys between", start, "and", end, "are"
        for i in range(len(sortedKeys)):
            if(start < sortedKeys[i] and sortedKeys[i] < end):
                print sortedKeys[i]
                if(self.hashTable[sortedKeys[i]] >= 2):
                    return True
        return False

    def addToBookingsBetweenStartAndEnd(self, start, end, sortedKeys):
        print "Addin to keys between", start, "and", end
        for i in range(len(sortedKeys)):
            if(start < sortedKeys[i] and sortedKeys[i] < end):
                print sortedKeys[i]
                self.hashTable[sortedKeys[i]] = self.hashTable[sortedKeys[i]] + 1 

    def findTrippleBookingsAtKey(self, key, sortedKeys):
        #if key already present in hash we know how many bookings it has
        if(key in self.hashTable):
            print "bookings at",key,"are",self.hashTable[key]
            if(self.hashTable[key] >= 2):
                return True, self.hashTable[key]
            return False, self.hashTable[key]
        #if key not present then we need to find a place between keys that are just less than current key and just greater than current key.
        for i in range(len(sortedKeys)):
            if(i>0 and (sortedKeys[i-1] < key and key < sortedKeys[i])):
                if(self.hashTable[sortedKeys[i-1]] >= 2):
                    print "bookings at",key,"are",self.hashTable[sortedKeys[i-1]]
                    return True, self.hashTable[sortedKeys[i-1]]
                else:
                    if(self.hashTable[sortedKeys[i-1]] < 0):
                        print "bookings at",key,"are",0
                        return False, 0
                    print "bookings at",key,"are",self.hashTable[sortedKeys[i-1]]
                    return False, self.hashTable[sortedKeys[i-1]]
        print "bookings at",key,"are",0
        return False, 0

    def insertInHashTable(self, start, end):
        print start, end
        if not self.hashTable:
            self.insertStartEndInHash(start, end, 0, 0)
            return True
        #Find all keys between start and end and add 1 to them
        sortedKeys = sorted(self.hashTable)
        print sortedKeys
        if (self.findTrippleBookingsBetweenStartAndEnd(start, end, sortedKeys)):
            return False
        flag, startAdder = self.findTrippleBookingsAtKey(start, sortedKeys)
        if(flag):
            return False
        flag, endAdder = self.findTrippleBookingsAtKey(end, sortedKeys)
        if(flag):
            return False
        self.addToBookingsBetweenStartAndEnd(start, end, sortedKeys)
        self.insertStartEndInHash(start, end, startAdder, endAdder)
        return True

    def book(self, start, end):
        print self.insertInHashTable(start, end)
        print self.hashTable
        """
        :type start: int
        :type end: int
        :rtype: bool
        """  

#Main
obj = MyCalendarTwo()
obj.book(10,20)
obj.book(50,60)
obj.book(10,40)
obj.book(5,15)
obj.book(5,10)
obj.book(25,55)
