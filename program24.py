#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    return map(lambda t: sum([x > y for x, y in zip(*t)]), ((a, b), (b, a)))



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()
