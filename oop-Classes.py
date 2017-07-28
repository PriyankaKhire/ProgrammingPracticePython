#OOP concepts: Class and class functions 

#Empty class, putting pass statement will let python know that this for now is an empty class
class EmptyClass:
    pass

class ClassName:
    class_variable = "some variable"
    
    def __init__(self, arg1, arg2):
        print "Inside the constructor"
        print "The self contains the object instance that looks like "+str(self)
        print "Now assiginig instance variables"
        self.arg1 = arg1
        self.arg2 = arg2
        print self.arg1
        print self.arg2
    
    def class_func(self):
        print "In class function"
        print "Now remember in python, the class functions ALWAYS take class instance as the first argument"
        print "So if you define this function without this self as argument then it wont work"

    def access_class_variable(self):
        print "To access class variable we need to use self too"
        return self.class_variable

    def setClassVariable(self, value):
        print "Setting class variable to a new value"
        self.class_variable = value

    @classmethod
    def class_method(cls):
        print "A class method will take a class instance cls"
        print "Class method instead of operating on single instance will operate on whole class instead"
        print "Class method can be used as alternative constructors too"
        print "We can use class method to create class objects"
        print "like here we will create and return the class object"
        return cls("argument one", "argument two")

    @staticmethod
    def static_method():
        print "A static method doesn't require an object instance or a class instance"
        print "They are just normal methods who in some way are related to class"
        print "but as mentioned above they don't require calss or object instance"
        

#Main Program
obj1 = ClassName(1,"abc")
print "Accessing the arguments from object instance "+str(obj1.arg1)+" "+str(obj1.arg2)
obj1.class_func()
print obj1.access_class_variable()
obj1.setClassVariable(123)
print obj1.access_class_variable()
print "In general it's always a good idea to create getters and setters to access class variables"
obj2 = ClassName.class_method()
print obj2
print "Calling static method from obj1"
obj1.static_method()
print "Calling static method from obj2"
obj2.static_method()
print "Calling static method from class instance"
ClassName.static_method()
