#Unique Email Addresses
#https://leetcode.com/problems/unique-email-addresses/
class Solution(object):
    def __init__(self):
        self.ht = {}

    def insertDomains(self, emails):
        #key is domain name and value is local name
        for email in emails:
            if not(email.split("@")[1] in self.ht):
                self.ht[email.split("@")[1]] = [email.split("@")[0]]
            else:
                self.ht[email.split("@")[1]].append(email.split("@")[0])
        print self.ht

    def processLocalName(self):
        outputSet = []
        for key in self.ht:
            for localName in self.ht[key]:
                #everything after first + sign is ignored
                name = ""
                for namePart in localName.split("+")[0].split("."):
                    name = name+namePart
                #insert name in outputSet
                emailAddress = name+"@"+key
                if not(emailAddress in outputSet):
                    outputSet.append(emailAddress)
        return outputSet
        
    def logic(self, emails):
        self.insertDomains(emails)
        return len(self.processLocalName())
            
    def numUniqueEmails(self, emails):
        print self.logic(emails)        
        """
        :type emails: List[str]
        :rtype: int
        """
#Main
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
obj = Solution()
obj.numUniqueEmails(emails)
