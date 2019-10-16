n = int(input())
s=0
t=0
while(n>0):
	rem= n%2
	if rem==1:
		s+=1
		if t<s:
			t=s
	else:
		s=0
	n=int(n/2)
print (t)