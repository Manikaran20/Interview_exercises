def review(S):
	
	ist=''
	sec=''
	for i in range(len(S)):
	    if i%2==0:
	        ist+=S[i]
	        
	    else:
	        sec+=S[i]
	       
	print (ist, sec)

T=int(input())
S=[]
for i in range(T):
		S.append(input())
for i in S:
	review(i)

