def highest_even(list):
    evens = []
    for num in list:
        if(num % 2 == 0):
            evens.append(num)
    
    highest_number = 0
    for even_num in evens:
        if(even_num > highest_number):
            highest_number = even_num
    
    return highest_number

print(highest_even([10, 2, 3, 4, 8, 11]))

