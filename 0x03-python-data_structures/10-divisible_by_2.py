#!/usr/bin/python3

def divisible_by_2(my_list=None):
    my_list = my_list or []
    
    for i in my_list:
        if i % 2 == 0:
            print("{:d} is divisible by 2".format(i))
        else:
            print("{:d} is not divisible by 2".format(i))