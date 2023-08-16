#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    t = 1
    roman_list = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] in roman_list:
            if roman_list.get(roman_string[i]) > roman_list.get(roman_string[i - 1]):
                r = roman_list.get(roman_string[i - 1])
                while r >= 10:
                    t *= 10
                    r /= 10
                num += 8 * t
            else:
                num += roman_list.get(roman_string[i])
        else:
            return None
    return num
