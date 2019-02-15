#Interleaving String
#https://leetcode.com/problems/interleaving-string/
class Approch1(object):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def fillMatrix(self, s1Index, s2Index, s3Index):
        #Using the dfs approch
        if(s3Index == len(self.s3)):
            if(s2Index == len(self.s2) and s1Index == len(self.s1)):
                return True
            return 
        #checking s1
        if(s1Index < len(self.s1) and self.s1[s1Index] == self.s3[s3Index]):
            #print "equal to S1 Index"
            if(self.fillMatrix(s1Index+1, s2Index, s3Index+1)):
                return True
        #checking s2
        if(s2Index < len(self.s2) and self.s2[s2Index] == self.s3[s3Index]):
            #print "equal to S2 Index"
            if(self.fillMatrix(s1Index, s2Index+1, s3Index+1)):
                return True
                
    def logic(self):
        if self.fillMatrix(0, 0, 0):
            return True
        return False
        
#Main
obj1 = Approch1("aaa", "bbb", "aab")
print obj1.logic()
