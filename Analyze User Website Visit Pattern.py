# Analyze User Website Visit Pattern
# https://leetcode.com/problems/analyze-user-website-visit-pattern/

class User(object):
    def __init__(self, username):
        self.name = username
        self.tsAndWebsites = {}
        self.sortedKeys = []
    
    def addWebsite(self, time, website):
        self.tsAndWebsites[time] = website
    
    def sortKeys(self):
        self.sortedKeys = sorted(self.tsAndWebsites.iterkeys())
    
    def groupThree(self, answer, index, websiteList):
        if(len(answer) == 3):
            websiteList.append(answer)
            return
        for i in range(index, len(self.sortedKeys)):
            websiteIndex = self.sortedKeys[i]
            website = self.tsAndWebsites[websiteIndex]
            self.groupThree(answer+[website], i+1, websiteList)
        
        
        
class Solution(object):
    def __init__(self):
        self.users = {}
        self.threeSequence = []
        self.threeSequenceCount = []
    
    def createUser(self, user):
        return User(user)
    
    def addToThreeSequenceCount(self, websiteList):
        if not(websiteList in self.threeSequence):
            self.threeSequence.append(websiteList)
            self.threeSequenceCount.append(0)
        # get index of list
        index = self.threeSequence.index(websiteList)
        self.threeSequenceCount[index] = self.threeSequenceCount[index]+1
    
    def addUsers(self, username, timestamp, website):
        for i in range(len(username)):
            # create user object if it doesn't exist
            if not(username[i] in self.users):
                userObj = self.createUser(username[i])
                self.users[username[i]] = userObj
            userObj = self.users[username[i]]
            # add website and time stamp
            userObj.addWebsite(timestamp[i], website[i])
            
            
    def mostVisitedPattern(self, username, timestamp, website):
        self.addUsers(username, timestamp, website)
        for user in self.users:
            #print user, self.users[user].tsAndWebsites
            # first sort the time stamp
            self.users[user].sortKeys()
            # group the 3 websites sorted according to time stamp
            websiteList = []
            self.users[user].groupThree([], 0, websiteList)
            # add the webiste list to 3 sequence
            for websites in websiteList:
                self.addToThreeSequenceCount(websites)
        #print self.threeSequence, self.threeSequenceCount
        maxVal = max(self.threeSequenceCount)
        index = self.threeSequenceCount.index(maxVal)
        return self.threeSequence[index]
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        
