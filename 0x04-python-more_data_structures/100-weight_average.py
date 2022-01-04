#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    promedio = 0
    mult = list([x[0] * x[1] for x in my_list])
    div = list([x[1] for x in my_list])
    promedio = sum(mult) / sum(div)
    return promedio
