#Wildcard Matching
#https://leetcode.com/problems/wildcard-matching/description/
class queue(object):
    def __init__(self):
        self.q = []

    def push(self, data):
        self.q.append(data)

    def pop(self):
        return self.q.pop(0)

    def top(self):
        return self.q[0]

    def empty(self):
        if not self.q:
            return True
        return False


class WildCardMatching(object):
    def __init__(self, s, p):
        self.s = s
        self.p = p
        self.qs = queue()
        self.qp = queue()

    def enqueue_strings(self):
        for char in self.s:
            self.qs.push(char)
        for char in self.p:
            self.qp.push(char)
        print "The queues now contain "+str(self.qp.q)+" "+str(self.qs.q) 

    def isMatch(self):
        self.enqueue_strings()
        #while both queues are not empty
        while not self.qs.empty() and not self.qp.empty():
            print "pattern queue is "+str(self.qp.q)
            print "string queue is "+str(self.qs.q)
            qpTop = self.qp.pop()
            print "top of pattern queue is "+str(qpTop)
            if qpTop == '*':
                #dequeue till you get a character
                while not self.qp.empty() and not self.qp.top().isalpha():
                    print "popped off "+str(slf.qp.top())
                    self.qp.pop()
                if self.qp.empty():
                    print "since qp is now empty and last character was * we ignore rest string"
                    #for case where s = "sdfs" p = "s**"
                    return True
                #Now pop the first char of pattern
                topChar = self.qp.pop()
                print "top alphabet of pattern after * is "+str(topChar)
                #dequeue the string q till you find top char in it
                while not self.qs.empty() and self.qs.top() != topChar:
                    print "dequeuing from string q, characters that are not equal to top char such as "+str(self.qs.top())
                    self.qs.pop()
                if self.qs.empty():
                    print "string q does not have maching pattern character and is now empty so we return false"
                    #for case where s = "bbbbbb" p = "*****a"
                    return False
                #now pop the top character off only if its equal
                while not self.qs.empty() and self.qs.top() == topChar:
                    print "now popping characters that are equal to top char of pattern q"
                    self.qs.pop()
            if qpTop == "?":
                #Pop just one character off
                if self.qs.empty():
                    print "since ? does not match empty character and string q is empty we return flase"
                    #because ? does not match empty character
                    return False
                print "popped off "+str(self.qs.top())+" from string q"
                self.qs.pop()
            if qpTop.isalpha():
                if self.qs.top() != qpTop:
                    print "Since top of string q is not equal to top of pattern q we return false"
                    return False
                print "Popped off "+str(self.qs.top())+" from string q"
                self.qs.pop()
        if self.qs.empty() and self.qp.empty():
            print "since both qs are empty we return true"
            return True
        print "since one of the queue is not empty we return flase"
        return False

#Main Program
#o = WildCardMatching("adceb", "*a*b")
o = WildCardMatching("abefcdgiescdfimde", "ab*cd?i*de")
print o.isMatch()
