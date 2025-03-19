import time
import math

def sqrtseconds(number, ms):
    seconds = ms / 1000.0
    time.sleep(seconds)
    
    return math.sqrt(number)

number = int(input())
ms = int(input())

result = sqrtseconds(number,ms)

print(f"Square root of {number} after {ms} milliseconds is {result}")

#25100
#2123