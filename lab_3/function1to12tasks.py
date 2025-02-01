def toOunces(grams) :
    ounces = grams *  28.3495231
    print(f'{grams} grams = {ounces} ounces\n')

def toCentigrade(f) :
    c = (5 / 9) * (f - 32)
    print(f'{c}\n')

def solve(numheads, numlegs):
    #x - chicken, y - rabbit
    #x+y = numheads   and     2x+4y=numlegs
    #x = numheads - y          2(numheads - y)+4y=numlegs
    #2numheads-2y+4y=numlegs
    #2y= numlegs-2numheads
    #y= (numlegs-2numheads)/2
    rabbit = (numlegs-2*numheads)/2
    chicken = numheads - rabbit

    print(f'There are {int(chicken)} chickens and {int(rabbit)} rabbits\n')

def filter_prime(list):
    cnt = 0
    for i in list:
        j = 1
        cnt = 0
        while(j <= i):
            if i % j == 0:
                cnt += 1
            j += 1
            if cnt > 2: break

        if cnt == 2:
            print(i, end = ' ')
    print('', end = '\n')

def permutations(str):
    from itertools import permutations
    for perm in permutations(str):
        print(''.join(perm))


def WordsReverse(str):
    newlist = str.split(' ')
    newlist.reverse()
    print(' '.join(newlist), end = '\n')

def has_33(nums):
    for i in range(len(nums) - 1): 
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True
    return False

def spy_game(nums):
    zerocnt = nums.count(0)
    if zerocnt < 2:
        return False
    else:
        first_0 = nums.index(0)
        nums[first_0] = 1
        second_0 = nums.index(0)
        seven = nums.index(7)
        if first_0 < second_0 and second_0 < seven:
            return True
        else:
            return False

def SphereVolume(r):
    import math
    print(f'Volume: {4 / 3 * math.pi * r**3}')

def UniqueElements(mylist):
    newlist = []
    for x in mylist:
        if x not in newlist:
            newlist.append(x)
    print(newlist)

def isPalinrome(str):
    strreverse = str[::-1]
    if strreverse == str:
        return True
    else:
        return False

def histogram(mylist):
    for i in mylist:
        while(i > 0):
            print('*', end='')
            i-=1
        print('',end = '\n')




'''toOunces(100)

toCentigrade(100)

solve(35, 94)

filter_prime([1,2,3,4,5,6,7,13,14,361,343,929])
print('', end = '\n')


WordsReverse('We are ready')
print('', end = '\n')

permutations("acb")


print(has_33([1,3,2,3,3]))
print(has_33([1,3,2,3,]))
print('', end = '\n')

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

print('', end = '\n')
SphereVolume(10)


print('', end = '\n')
UniqueElements([1,1,1,2,3,4,2,4,45,2,3,3,3,3,3])

print('', end = '\n')

print(isPalinrome("madam"))
print(isPalinrome("hello"))
print('', end = '\n')


histogram([4, 9, 7,13,1,20,5])'''