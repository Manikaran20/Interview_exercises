def fun(s):
    atoz=[]
    sl=list(map(str, range(0,10)))
    for i in range(ord('a'), ord('z')+1):
        atoz.append(chr(i))
    a=s.split('@')
    try:
        b=a[1].split('.')
    except:
        return False
    l=[a[0]]+b
    if '' in l:
        return False
    if (len(l)!=3):
        return False
    for i in l[0]:

        if i in atoz or i in sl or i in ['-', '_']:
            print ('b', i)
            continue
        else:
            print ('c')
            return False
    for i in l[1]:
        if i in atoz or i in sl:
            continue
        else:
            return False

    if len(l[2])>3:
        return False

    return True 
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)