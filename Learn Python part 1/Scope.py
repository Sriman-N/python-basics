# Scope - what variables do I have access to?

# global scope (everyone can access this variable)
def some_func():
    total = 100

#print(total) #won't work

if True:
    x = 10

print(x) #will work

#Scope rules the python interpretor follows:
#1 - Start with local
#2 - Parent local?
#3 - Global
#4 - built in python functions