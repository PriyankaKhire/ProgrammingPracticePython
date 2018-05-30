#Edit distance
#https://jlordiales.me/2014/03/01/dynamic-programming-edit-distance/

class editFunctions():
    #insert a char, at given position in the string
    def insert(self, pos, char, string):
        return string[:pos]+char+string[pos:]

    def delete(self, pos, string):
        return string[:pos]+string[pos+1:]

    #replace a character at given pos with another 'char' in the string
    def replace(self, pos, char, string):
        return string[:pos]+char+string[pos+1:]
    

class backTrackingMethod(editFunctions):
    #Perform actions on s1 to convert it into s2
    def logic(self, s1, s2, editCount, editAction, s1Index, s2Index):
        #return condition
        if(s1 == s2):
            print "Edit distance "+str(editCount)
            return
        new_s1 = ""
        #what is the current action that needs to be taken on the string
        if editAction == "insert":
            print "inserting "+s2[s2Index]+" at position "+str(s1Index)+" in "+s1
            new_s1 = self.insert(s1Index,  s2[s2Index], s1)
        elif editAction == "delete":
            print "deleting "+s1[s1Index]+" from "+s1
            new_s1 = self.delete(s1Index, s1)
        elif editAction == "replace":
            print "replacing "+s1[s1Index]+" of "+s1+" with "+s2[s2Index]
            new_s1 = self.replace(s1Index, s2[s2Index], s1)
        #get new s2Index
        if s1[s1Index] == s2[s2Index]:
            s2Index = s2Index + 1
        print new_s1
        self.logic(new_s1, s2, editCount+1, "insert", s1Index+1, s2Index)
        self.logic(new_s1, s2, editCount+1, "delete", s1Index+1, s2Index)
        self.logic(new_s1, s2, editCount+1, "replace", s1Index+1, s2Index)

    def solution(self, s1, s2):
        self.logic(s1, s2, 0, "insert", 0, 0)
        self.logic(s1, s2, 0, "delete", 0, 0)
        self.logic(s1, s2, 0, "replace", 0, 0)

#Main Program
obj = backTrackingMethod()
obj.solution("abc", "ac")
        
            
