#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    int_arguments = [int(arg) for arg in arguments]
    result = sum(int_arguments)
    print(result)
