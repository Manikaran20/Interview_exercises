# Enter your code here. Read input from STDIN. Print output to STDOUT
m=input()
a=input().split()
M=set(a)
n=input()
b=input().split()
N=set(b)
s=(M.union(N)).difference(M.intersection(N))
l=list(s).sort()
for i in s:
    print (i)



