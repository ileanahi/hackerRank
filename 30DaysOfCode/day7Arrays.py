#!/bin/python

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for i in range(1,len(arr)+1):
    print arr[len(arr)-i],
    i+=1
