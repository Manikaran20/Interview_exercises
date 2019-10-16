#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expsd,mfected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    l=[]
    c=0
    for i in range(max(a),min(b)+max(a),max(a)):
        l.append(i)
    print (l)
    for i in l:
        for j in a:
            if i%j==0:
                print (i,j)
                flag=True
                continue
            else:
                flag=False
                break
        if flag==True:
            for k in b:
                if k%i==0:
                    print (k,i)
                    flag=True
                    continue
                else:
                    flag= False
                    break
            if flag==True:
                c+=1
        else:
            continue
    return c



            

    

    # Write your code here

if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print (total)
