#Bulls and Cows
#https://leetcode.com/problems/bulls-and-cows/
class Solution(object):
    
    def stringRemoveCharAt(self, string, index):
        return string[:index]+string[index+1:]
    
    def findBulls(self, secret, guess):
        index = 0
        bullCount = 0
        while(index < len(secret)):
            if(secret[index] == guess[index]):
                bullCount = bullCount + 1
                secret = self.stringRemoveCharAt(secret, index)
                guess = self.stringRemoveCharAt(guess, index)
            else:
                index = index + 1
        return bullCount, secret, guess

    def putInHash(self, secret):
        ht = {}
        for char in secret:
            if not(char in ht):
                ht[char] = 1
            else:
                ht[char] = ht[char]+1
        return ht

    def findCows(self, secret, guess):
        ht = {}
        #Store numbers of secret in hashTable along with their count.
        ht = self.putInHash(secret)
        cowCount = 0
        for char in guess:
            if(char in ht and ht[char] > 0):
                cowCount = cowCount + 1
                ht[char] = ht[char] - 1
        return cowCount
        
    def getHint(self, secret, guess):
        bullCount, secret, guess = self.findBulls(secret, guess)
        cowCount = self.findCows(secret, guess)
        print str(bullCount)+"A"+str(cowCount)+"B"
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

#Main
obj = Solution()
obj.getHint('1807', '7810')
