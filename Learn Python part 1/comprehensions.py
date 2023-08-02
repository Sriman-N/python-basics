#list, set, dictionary comprehensions

#list comprehensions
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

#my_list = [param for param in iterable if expression] (param means variable) (iterable meaning list, set, dictionary, string)
#first param is what we want to do with the data from the second param
#second param is to extract from iterable
my_list2 = [x for x in 'hello'] 
my_list3 = [num for num in range(0, 100)]
my_list4 = [num*2 for num in range(0, 100)]

my_list5 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list2)
print(type(my_list2))
print(my_list3)
print(my_list4)
print(my_list5)

#set comprehensions
#my_list = {param for param in iterable if expression} (param means variable) (iterable meaning list, set, dictionary, string)
#first param is what we want to do with the data from the second param
#second param is to extract from iterable
my_list2 = {x for x in 'hello'}
my_list3 = {num for num in range(0, 100)}
my_list4 = [num*2 for num in range(0, 100)]

my_list5 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_list2)
print(type(my_list2))
print(my_list3)
print(my_list4)
print(my_list5)

#dictionary comprehensions
#my_dict = {param for param in iterable if expression} (param means variable) (iterable meaning list, set, dictionary, string)
#first param is what we want to do with the data from the second param
#second param is to extract from iterable
simple_dict = {
    'a':1,
    'b':2
}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)

