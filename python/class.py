# define a class named Student 
# Student is inherit object
class Student(object):
    # self is the default param likes this
    def __init__(self,name,age):
        self.name = name
        # private property begin with __
        self.__age = age
        self.__gender = "female"

    # self is the default param in other method
    def hello(self):
        print("hello i am",self.name)
        return

    # define getter and setter

    # decorator pattern
    def get_age(self):                                return self.__age

    def set_age(self,i=12):
        self.__age = i
        return
    @property
    def gender(self):
        return self._gender
    # they both have the same name!!!
    @gender.setter
    def gender(self,g):
        self._gender = g
    # order is very very very important for every script(maybe) language



# caution: there is no 'new' when new a object
# which aften used in c++ java even js
stu = Student("12tall",12)
stu.hello()
print(stu.name)
# private prop can not be used directly
# print(stu.__age)
# when using @property the method should be using as a common property,not a function ever
print(stu.get_age())
stu.gender = 1
print(stu.gender)

# in other language using interface to implement polymorphic(duotai)
# in script overwrite the base's method 

# isinstance = is a instanc of base class
print(type(stu))

# dir like reflection,can get all propertis of an object
# hasattr(),setattr(),getattr() can operate attribute of an object
print(dir(stu))
# by import Module types
# can show whether the property is a function,lambda etc.
