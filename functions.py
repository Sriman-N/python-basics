def func1():
    print("Hello")

def power(first, second=1):
    result = 1
    for i in range(second):
        result = result * first;
    return result;

# function with variable number of arguments
def multi_add(*args): #  * means variable number of arguments 
    result = 0
    for x in args:
        result = result + x
    return result


print(power(4))
print(power(2,3))
print(power(second=4,first = 2))

print(multi_add(4,2,5,6,10,4,2))