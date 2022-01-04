#!/usr/bin/python3
def roman_to_int(roman_string):
    romano = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    arabigo = []
    largo = len(roman_string)
    suma = 0
    for i in roman_string:
        arabigo.append(romano[i])
    if largo == 1:
        return romano[roman_string]
    else:
        for i in range(1, largo):
            if arabigo[i - 1] < arabigo[i]:
                arabigo[i - 1] = -arabigo[i - 1]
        for ara in arabigo:
            suma += ara
        return suma
