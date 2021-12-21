#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if((i != 8 or j != 9) and (i < j)):
            print("{}{}".format(i, j), end=", ")
print("89")
