
def pallindrome(string):
	flag=False
	l=len(string)

	for i, j in zip(range(0,l/2), range(-1,-l/2,-1)):
		print(string[j])
		if(string[i]==string[j]):
			flag=True
		else:
			flag=False

	if(flag==True):
		print("pallindrome")
	else:
		print("not a pallindrome")


pallindrome("mabaabm")