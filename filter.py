#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    l=[]
    p=0
    for i in ar:
        if i in l:
            continue
        else:
            l.append(i)
            f=filter(lambda x: x==i, ar)
            p+=len(list(f))//2
    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
