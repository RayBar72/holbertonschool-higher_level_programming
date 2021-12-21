#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    first = -number % 10 * -1
else:
    first = number % 10
print("Last digit of", number, "is", first, end=" ")
if first == 0:
    print("and is 0")
elif first > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
