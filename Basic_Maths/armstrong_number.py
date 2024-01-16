from os import *
from sys import *
from collections import *
from math import *

n = int(input())
m = n
n = str(n)
ans = 0
for i in range(len(n)):
    ans = ans + int(n[i])**len(n)
if(ans == m):
    print("true")
else:
    print("false")