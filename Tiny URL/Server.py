#Server
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
    
    class Approch1(object):
        def hashFunctionUsingMd5(self, string):
            return md5.new(string).hexdigest()

        def issueWithApproch(self):
            print "Generates a hash value of 32 chars but we only want 8"

        def solution1(self, hashString):
            print "to tackle this issue we can take following approch"
            return hashString[0:8]

        def cons(self):
            print "Need to finish this"
    
class Server(object):
    def __init__(self):
        self.exp = Explanation()
        #self.encodeUrlApproch1 = EncodingURL().Approch1().cons()
        self.id = 1

    def removePrefix(self, prefix, string):
        if(string.startswith(prefix)):
            return string[len(prefix):]
        return string

    def removeCommonPrefixes(self, url):
        prefixes = ["https://","http://","www."]
        for prefix in prefixes:
            url = self.removePrefix(prefix, url)
        return url

    def shortenURL(self, url):
        url = self.removeCommonPrefixes(url)
        self.exp.explanation1()
        
        
        

#Main
obj = Server()
obj.shortenURL("www.google.com")
