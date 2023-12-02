#!/usr/bin/python3
from sys import argv

def print_arguments():
    # get the numbers of arguments
    num_arguments = len(argv) - 1  # Subtracting 1 to exclude the script name itself
    print(f"Number of argument{'s' if num_arguments != 1 else ''}: {num_arguments}", end="")

    if num_arguments == 0:
        print(".")
    else:
        print(":")
        # Print each argument along with its position
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
