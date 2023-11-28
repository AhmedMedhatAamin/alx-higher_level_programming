#!/usr/bin/python3
try:
    for i in range(0, 100):
        print("{:02}".format(i), end=", " if i < 99 else "\t")
except Exception as e:
    print(f"[Error]: {e}")
