
#lists are mutable
a, b, c, * other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)


#tuples are unmutable (no modification)
my_tuple = (1, 2, 3, 4, 5, 6)
print(5 in my_tuple)

x = my_tuple[0]

x, y, z, *other = (1, 2, 3, 4, 5)

#dictionary

my_dict = {
    'a': "bike",
    'b': "car",
    'c': 2,
    'basket': [1, 2, 3]
}

print(my_dict['a'])

#Sets 
my_set = {1, 2, 3, 4, 5}
print(my_set)
#returns {1, 2, 3, 4, 5}

my_set2 = {1, 2, 3, 4, 5, 5}
print(my_set2)
#returns {1, 2, 3, 4, 5} (already has the second five)

my_set.add(100)
my_set.add(2) #does not have a second 2