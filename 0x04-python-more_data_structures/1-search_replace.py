#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for listo in my_list:
        if listo == search:
            new_list.append(replace)
        else:
            new_list.append(listo)
    return new_list
