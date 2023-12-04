#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result_list = []
    
    if len(my_list) > 0:
        for i in my_list:
            if i % 2 == 0:
                print("{:d} is divisible by 2".format(i))
                result_list.append(True)
            else:
                print("{:d} is not divisible by 2".format(i))
                result_list.append(False)
    else:
        return result_list
