def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1): #проверяем только до корня числа 
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
