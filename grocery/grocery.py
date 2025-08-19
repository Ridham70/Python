l = {}
while 1:
    try:
        i = input().strip().upper()
        if i in l :
            l[i] += 1
        else:
            l[i] = 1
    except EOFError:
        for k in sorted(l.keys()):
            print(l[k], k)
        break

