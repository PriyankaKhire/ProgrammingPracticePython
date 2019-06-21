#Unique Email Addresses
#https://leetcode.com/problems/unique-email-addresses/
class Solution(object):
    def processAddress(self, address):
        print address
        newAddress = ""
        for char in address:
            if(char == "."):
                continue
            if(char == "+"):
                return newAddress
            newAddress = newAddress+char
        return newAddress
        
    def numUniqueEmails(self, emails):
        ht = {}
        for email in emails:
            splitEmail = email.split("@")
            domain = splitEmail[1]
            address = self.processAddress(splitEmail[0])            
            if not(domain in ht):
                ht[domain] = [address]
            else:
                if not(address in ht[domain]):
                    ht[domain].append(address)
        #Count the emails in hash table
        emailCount = 0
        for key in ht:
            emailCount = emailCount + len(ht[key])
        print emailCount
        """
        :type emails: List[str]
        :rtype: int
        """
#Main
obj = Solution()
obj.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
