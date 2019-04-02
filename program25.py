'''The first line contains two space-separated integers n and d, the size of a and the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Output Format

Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.'''
import math
import os
import random
import re
import sys

def rotLeft(a,n, k):
    alist = list(a)
    b = alist[k:]+alist[:k]
    return b

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a,n, d)
    print(result)
