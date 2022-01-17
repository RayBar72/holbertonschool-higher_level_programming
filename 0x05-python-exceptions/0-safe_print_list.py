#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except (ValueError, IndexError, TypeError):
        pass
    finally:
        print()
        return i
