#Fundamental Data Types
#int number 3, 4, 5 (inludes negative numbers)
#float number 3.2, 5.1234789, (With decimals)
#bool
#str
#list
#tuple
#set 
#dict

print(type(2+4))


#Classes -> custom types

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printThis(self):
        return self.name + " is " + self.age + " years old"

p1 = Person("Sriman", 32)
print(p1.printThis)

#Specialized Data Types

#None #means nothing