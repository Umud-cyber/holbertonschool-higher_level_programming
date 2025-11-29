#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1 / my_list_2
        except TypeError:
            print("wrong")
            result = 0
        except ZeroDivisionError:
            print("it's an error")
            result = 0
        except IndexError:
            print("it's out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
