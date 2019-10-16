n = int(input())
s = set(map(int, input().split()))
N=int(input())
for _ in range(N):
    cmd=input()
    if cmd== 'pop':
        s.pop()
    else:
        l=cmd.split()
        command='s.'+l[0]+'('+l[1]+')'
        eval(command)
T=list(s)
print (sum(T))

