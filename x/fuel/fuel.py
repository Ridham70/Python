while 1:
    try:
        n, d = input("Fraction: ").split("/")
        f = int(n)/int(d)
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
p = round(f*100)
if p <= 1 :
    print("E")
elif p >= 99 :
    print("F")
else:
    print(f"{p}%")
