#OOP concepts: Inheritance

class BaseClass:
    class_variable = "Base class variable"

    def __init__(self):
        print "inside base class constructor"

    def getClassVariable(self):
        return self.class_variable

    def setClassVariable(self, value):
        self.class_variable = value

    @classmethod
    def class_method(cls):
        print cls

    @staticmethod
    def static_method():
        print "inside base class static method"

class ChildClass(BaseClass):
    pass
class ChildClassWithConstructor(ChildClass):
    def __init__(self):
        print "*****"
        print "The below statement lets it inherite functionality of init method of child class"
        ChildClass.__init__(self)
        print "inside child class with constructor"
        print "*****"
#Main Program
#Base class
base_obj = BaseClass()
base_obj.setClassVariable(123)
print base_obj.getClassVariable()
BaseClass.class_method()
BaseClass.static_method()
#ChildClass
child_obj = ChildClass()
print help(child_obj)
#Child class with constructor
child_constructor_obj = ChildClassWithConstructor()
print help(child_constructor_obj)
