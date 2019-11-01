#!/bin/python3
import sys
import os
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    l=[]
    rank=[1]
    scores=list(set(scores))
    scores.sort(reverse=True)
    for alice_s in alice:
        if alice_s>=scores[0]:
            l.append(1)
        elif alice_s==scores[-1]:
            l.append(len(scores))
        elif alice_s<scores[-1]:
            l.append(len(scores)+1)
        else:
            l.append(binary_search(scores,alice_s))

    return l




def binary_search(arr,element):
    hi=len(arr)-1
    lo=0
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if arr[mid]==element:
            return mid+1
        elif element>arr[mid]:
            if element<arr[mid-1]:
                return mid+1
            elif element==arr[mid-1]:
                return mid
            else:
                hi=mid-1
        else:
            if element>=arr[mid+1]:
                return mid+2
            else:
                lo=mid+1
    return -1
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
