#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        news = [list for list in reversed(my_list)]
        for new in news:
            print("{:d}".format(new))
