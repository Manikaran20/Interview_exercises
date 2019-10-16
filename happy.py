n=input().split()
arr= list(input().split())
A=input().split()
B=input().split()
A=set(A)
B=set(B)
c=set(arr)
print (A,B,c)
s=0
for i in c:
	if i in A:
		s+=1
	elif i in B:
		s-=1



print (s)
