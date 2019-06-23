#Subdomain Visit Count
#https://leetcode.com/problems/subdomain-visit-count/
class Solution(object):
    def __init__(self):
        self.ht = {}
        
    def countSubDomain(self, visitCount, domain):
        domainSplit = domain.split(".")
        for i in range(len(domainSplit)):
            key = ".".join(domainSplit[i:])
            if not(key in self.ht):
                self.ht[key] = visitCount
            else:
                self.ht[key] = self.ht[key] + visitCount
        
    def subdomainVisits(self, cpdomains):
        for cpdomain in cpdomains:
            domainSplit = cpdomain.split(" ")
            self.countSubDomain(int(domainSplit[0]), domainSplit[1])
        output = []
        for key in self.ht:
            string = str(self.ht[key])+" "+key
            output.append(string)
        print output
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
#Main
obj = Solution()
obj.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
