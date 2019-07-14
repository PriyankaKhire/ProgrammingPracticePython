#Find Duplicate File in System
#https://leetcode.com/problems/find-duplicate-file-in-system/
    
class Solution(object):
    def findDuplicate(self, paths):
        ht = {}
        for path in paths:
            splittedPaths = path.split(" ")
            directory = splittedPaths[0]
            if(len(splittedPaths) <= 1):
                continue
            for i in range(1, len(splittedPaths)):
                fileAndContent = splittedPaths[i].split("(")
                fileName = directory+"/"+fileAndContent[0]
                content = fileAndContent[1][:-1]
                if not(content in ht):
                    ht[content] = [fileName]
                else:
                    ht[content].append(fileName)
        output = []
        for key in ht:
            if(len(ht[key]) > 1):
                output.append(ht[key])
        print output
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
#Main
obj = Solution()
#obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])

obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"])
