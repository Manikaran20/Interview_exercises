def timeConversion(s):
    h=int(s[0:2])
    ampm=s[-2]
    if ampm=="A" and h != 12:
        return s[:-2]
    elif ampm=="A" and h==12:
        return ("00"+s[2:-2])
    elif ampm=="P" and h<12:
        p=str(h+12)
        s=p+s[2:]
        return s[0:-2]
    elif ampm=="P" and h==12:
        return (s[0:-2])
s=str(input())
a=timeConversion(s)
print (a)