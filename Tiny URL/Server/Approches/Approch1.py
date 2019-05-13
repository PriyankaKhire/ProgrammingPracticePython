#md5 approch to encode url.
import sys
sys.path.append("../../..")
from ColorText import ColorText
import md5
class Explanation(object):
    
    def explanation1(self):
        print "The approch is to take every url and generate a hash value for it"
        print "and store in hash table such that key is hash value and value is the url."
        print "So that the final output would be "
        print "URL -> tinyURL -> www.tinyurl.com/<hashValue>"
        print "This www.tinyurl.com/<hashValue> should take you to your original URL page"

    def explanation2(self):
        print "The hash value should be unique"
        print "Now we have dicided on hash string size of 8"

class EncodingURL(object):
    def __init__(self):
        self.ct = ColorText()
        self.exp = Explanation()
    
    def hashFunctionUsingMd5(self, string):
        return md5.new(string).hexdigest()

    def issueWithApproch(self):
        self.ct.display("Generates a hash value of 32 chars but we only want 8", "dark-red")

    def solution1(self, hashString):
        self.ct.display("to tackle this issue we can take following approch", "green")
        return hashString[0:8]

    def con1(self):
        self.ct.display("This approch can produce duplicate keys", "light-red")
        self.ct.display("For example, what if hash value of google.com is 123456789101112131415", "light-red")
        self.ct.display("and hash value of yahoo.com is 123456781514131211109", "light-red")
        self.ct.display("since we discard last 13 characters this can produce duplicate keys", "light-red")

    def solution2(self):
        self.ct.display("Another solution is to append an ever increasing sequence of numbers to the hash value", "green")

    def con2(self):
        self.ct.display("but what if this ever increasing number becomes too big ?", "light-red")

    def solution3(self):
        self.ct.display("Append the unique user id to hash value", "green")

    def con3(self):
        self.ct.display("What if user is not signed in? then we can ask user to chose a unique number", "light-red")
        self.ct.display("But this is also not a very good approch", "light-red")

    def run(self, string):
        self.ct.display(4*"\t"+"Approch1", "black-highlight")
        self.exp.explanation1()
        print "\n"
        self.exp.explanation2()
        hashString = self.hashFunctionUsingMd5(string)
        print "\nThe hash value for ", string, " is ", hashString
        print "\n"
        self.issueWithApproch()
        print "\n"
        print self.solution1(hashString)
        print "We have only taken first 8 characters and chopped rest of them\n"
        self.con1()
        print "\n"
        self.solution2()
        print "\n"
        self.con2()
        print "\n"
        self.solution3()
        print "\n"
        self.con3()

#Main
obj = EncodingURL()
obj.run("google.com")
        
