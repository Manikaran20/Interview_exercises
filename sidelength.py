N=int(input())
def answerr(l1,l):
    c=0
    for _ in range(l1):
        i=l[0]
        j=l[-1]
        print(i,j)
        s= i if i>j else j
        l.remove(s)
        if c==0:
            t=s
        c+=1
        print (s,t)
        if s>t:
            return ("No")
        else:
            t=s
    return ("Yes")
def answer(l1,l):
    t=100
    half=int(l1/2)
    for i, j in zip(range(half), range(-1,-half-1,-1)):
        s= l[i] if l[i]<=l[j] else l[j]
        if t<s:
            return("No")
        else:
            t=s
    if l1%2!=0:
        if t<l[half]:
            return ("No")
        else:
            return ("Yes")
    else:
        return ("Yes")
for _ in range(N):
    l=[]
    l1=int(input())
    l=(input().split())
    l=list(map(int,l))
    print (answerr(l1,l))



# Enter your code here. Read input from STDIN. Print output to STDOUT

