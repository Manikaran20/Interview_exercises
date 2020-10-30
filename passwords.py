#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'passwordCracker' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt


def passwordCracker(passwords, loginAttempt):
    l1=len(passwords)
    s=loginAttempt
    S=''
    counter=0
    passwords.sort(key=len,reverse=True)

    for i, j in zip(passwords,range(l1)):
        if i in s:
            t= re.subn(i,str(j),s)
            s=t[0]
    y=re.search("[a-z]",s)
    print (s)
    if (y):
        print ("WRONG PASSWORD")
    else:
        for i in s:
            counter+=1
            if (counter== len(s)):
                S+= (passwords[int(i)])
            else:
                S+= (passwords[int(i)]+' ')
        print (S)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        passwordCracker(passwords, loginAttempt)

       
