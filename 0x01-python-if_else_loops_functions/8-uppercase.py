#!/usr/bin/python3
def uppercase(str):
    for st in str:
        st = ord(st)
        if st >= 97 and st <= 122:
            st = st - 32
        print("{:c}".format(st), end="")
    print("")
