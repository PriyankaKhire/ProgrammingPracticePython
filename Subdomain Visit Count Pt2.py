# Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/description/

class Solution(object):
    def __init__(self):
        # key = domain name, value = count
        self.domainHash = {}
    
    def getDomains(self, cpdomains):
        for domains in cpdomains:
            array = domains.split(" ")
            visitCount = array[0]
            domainNames = array[1].split(".")
            # get all the subdomains
            subDomain = ""
            for d in reversed(domainNames):
                subDomain = d +"."+ subDomain
                subDomainName = subDomain[:-1]
                if (subDomainName not in self.domainHash):
                    self.domainHash[subDomainName] = 0
                # increment the count
                self.domainHash[subDomainName] += int(visitCount)
    
    def getList(self):
        # create a list from the hash
        output = []
        for key in self.domainHash:
            output.append(str(self.domainHash[key]) +" "+ key)
        return output

    def subdomainVisits(self, cpdomains):
        self.getDomains(cpdomains)
        return self.getList()
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
