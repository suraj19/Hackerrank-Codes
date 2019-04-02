'''Given an array of integers, find the sum of its elements.

For example, if the array ar=[1,2,3], 1+2+3=6, so return 6'''
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    return sum(ar[0:len(ar)])

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
