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
        self.threeSequenceHash = {}
    
    def createUser(self, user):
        return User(user)
    
    def addToThreeSequenceCount(self, websiteList):
        key = ','.join(websiteList)
        if not (key in self.threeSequenceHash):
            self.threeSequenceHash[key] = 0
        self.threeSequenceHash[key] = self.threeSequenceHash[key] + 1
    
    def getLexographicallySortedAnswer(self):
        # Find max value
        maxKeyValue = max(self.threeSequenceHash, key=self.threeSequenceHash.get)
        # Add all keys with lexographic value to array and sort them
        lexographicSortArray = []
        for key in self.threeSequenceHash:
            if (self.threeSequenceHash[key] == self.threeSequenceHash[maxKeyValue]):
                lexographicSortArray.append(key)
        return sorted(lexographicSortArray)
    
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
        print sorted(timestamp)
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
        answer = self.getLexographicallySortedAnswer()
        return answer[0].split(",")
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        
