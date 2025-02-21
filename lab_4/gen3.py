def divisible3_4(n):
    for i in range(n + 1): 
        if i % 3 == 0 and i % 4 == 0:  
            yield i  

n = 50  
for num in divisible3_4(n):
    print(num)
