n = int(input())
l = []
for _ in range(n):
	inputs=input().split()
	args=inputs[1:]
	cmd=inputs[0]
	if cmd!="print":
		cmd+="("+','.join(args)+')'
		eval("l."+cmd)
	else:
		print (l)