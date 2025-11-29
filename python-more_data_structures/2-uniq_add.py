#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = []
    total = 0

    for x in my_list:
        if x not in unique_numbers:
            unique_numbers.append(x)
            total += x

    return total
