#Edit distance
#https://jlordiales.me/2014/03/01/dynamic-programming-edit-distance/

class editFunctions():
    #insert a char, at given position in the string
    def insert(self, pos, char, string):
        print "Inserting "+char+" at position "+str(pos)+" in string "+string
        return string[:pos]+char+string[pos:]

    def delete(self, pos, string):
        print "deleting "+string[pos]+" at pos "+str(pos)+" from string "+string
        return string[:pos]+string[pos+1:]

    #replace a character at given pos with another 'char' in the string
    def replace(self, pos, char, string):
        print "replacing "+string[pos]+" with "+char+" in string "+string+" at position "+str(pos)
        return string[:pos]+char+string[pos+1:]
    

class backTrackingMethod(editFunctions):
    def __init__(self):
        self.actions = ["insert", "delete", "replace"]
    #Perform actions on s1 to convert it into s2
    def logic(self, s1, s2, s1i, s2i, ed):
        if(len(s1) < len(s2)):
            return
        if(s1 == ""):
            return
        if(s1 == s2):
            print "edit distance "+str(ed)
            return        
        #Moving on
        #print s1i, len(s1), s2i, len(s2)
        while(s1i < len(s1) - 1 and s2i < len(s2) - 1 and s1[s1i] == s2[s2i]):
            s1i = s1i+1
            s2i = s2i+1
        #delete end string
        if(len(s1) > len(s2) and s1[s1i] == s2[s2i] and s2i == len(s2)-1):
            print "edit distance "+str(ed+len(s1)-s1i-1)
            return
        for action in self.actions:
            new_s1 = ""
            if(action == "insert"):
                new_s1 = self.insert(s1i, s2[s2i], s1)
            if(action == "delete" and s1i < len(s1)):
                new_s1 = self.delete(s1i, s1)
            if(action == "replace" and s1i < len(s1)):
                new_s1 = self.replace(s1i, s2[s2i], s1)
            print "new s1 after editing it is "+new_s1
            self.logic(new_s1, s2, s1i, s2i, ed+1)
        

#Main Program
obj = backTrackingMethod()
obj.logic("horse", "ros", 0, 0, 0)
#string 1 should be always bigger than s2        
            
