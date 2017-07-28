#OOP concepts: Class and class functions 

#Empty class, putting pass statement will let python know that this for now is an empty class
class EmptyClass:
    pass

class ClassName:

    def __init__(self, arg1, arg2):
        print "Inside the constructor"
        print "The self contains the object instance that looks like "+str(self)
        print "Now assigning arguments"
        self.arg1 = arg1
        self.arg2 = arg2
        print self.arg1
        print self.arg2
    
    def class_func(self):
        print "In class function"
        print "Now remember in python, the class functions ALWAYS take class instance as the first argument"
        print "So if you define this function without this self as argument then it wont work"


#Main Program
obj1 = ClassName(1,"abc")
print "Accessing the arguments from object instance "+str(obj1.arg1)+" "+str(obj1.arg2)
obj1.class_func()

