def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

#Rule for order of the parameters: params, *args, default parameters, **kwargs
#example
def example(name, *args, i='hi', **kwargs):
    return None