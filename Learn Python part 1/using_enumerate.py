#enumerate

for i, char in enumerate('Helllooo'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char is 50:
        print(f'index of 50 is: {i}')