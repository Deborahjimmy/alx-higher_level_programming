#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            j = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            j = 0
        except TypeError:
            print("wrong type")
            j = 0
        except IndexError:
            print("out of range")
            j = 0
        finally:
            result.append(j)
    return result
