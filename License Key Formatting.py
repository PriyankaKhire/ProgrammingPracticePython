#License Key Formatting
#https://leetcode.com/problems/license-key-formatting/
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        #Convert S to upper
        S = S.upper()
        #remove all dashes
        S = ''.join(S.split("-"))
        charactersInFirstGroup = len(S)%K
        output = ''
        if(charactersInFirstGroup != 0):
            output =  '-'+S[0:charactersInFirstGroup]
        for i in range(len(S)/K):
            output = output + '-' + S[(i*K)+charactersInFirstGroup: (i+1)*K + charactersInFirstGroup]
        print output[1:]
            

#Main
obj = Solution()
obj.licenseKeyFormatting('sd-fs-j4-9-k', 4)
