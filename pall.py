def pall(string):
	l=len(string)
	for i,j in zip(range(0,l/2), range(-l,-(l/2))):
		print(i,j)
		if(string[i]==string[j]):
			flag=True
		else:
			flag=False
			break
	if(flag==False):
		print("Not a Pallidrome")
	else:
		print("Pallidrome")
if(__name__=="__main__"):
	pall("ruur")
