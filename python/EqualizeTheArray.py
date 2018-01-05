#!/bin/python

import sys

def equalizeArray(arr):
    # Complete this function
    return (n - max(arr.count(i) for i in arr))

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = equalizeArray(arr)
    print result
