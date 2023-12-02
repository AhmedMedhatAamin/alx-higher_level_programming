#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    my_len_list = len(my_list) - 1
    if idx < 0 or idx >= my_len_list:
        return None
    else:
        my_list[idx] = new_element
        return my_list
