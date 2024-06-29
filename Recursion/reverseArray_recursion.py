from os import *
from sys import *
from collections import *
from math import *

def reverseArrayHelper(l,r,arr):
    if l >= r:
        return arr
    arr[l],arr[r] = arr[r],arr[l]
    return reverseArrayHelper(l+1,r-1,arr)

def reverseArray(arr, m):
    # Write your code here.
    return reverseArrayHelper(m+1,len(arr)-1,arr)
