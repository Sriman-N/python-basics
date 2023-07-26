#Iterables
#iterable - list, dictionary, tuple, set, string
#iterated - one by one check each item in the collection

user = {
    'name': "Golem",
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)
print()
for item in user.items():
    print(item)
print()
for item in user.values():
    print(item)
print()
for item in user.keys():
    print(item)
print()
for key, value in user.items():
    print(key, value)