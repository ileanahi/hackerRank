<<<<<<< HEAD
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
=======
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
>>>>>>> e915652e0005753e5b2899f7b5b9b443be34aacb
