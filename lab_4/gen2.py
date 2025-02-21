def generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i 

n = 16
for square in generator(n):
    print(square, end = ', ')
