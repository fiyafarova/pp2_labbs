def square_generator(a,b):
    for i in range(a, b + 1):
        yield i ** 2  

a = 5
b = 13  

for square in square_generator(a,b):
    print(square)
