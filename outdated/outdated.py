month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while 1:
    i = input("Date: ")
    try :
        m, d, y = i.split("/")
        m, d, y = int(m), int(d), int(y)
        if 1 <= m <= 12 and 1 <= d <= 31 and y >= 1 :
            print(f"{y:04}-{m:02}-{d:02}")
            break
    except ValueError :
        pass
    try :
        m_d, y = i.split(", ")
        m, d = m_d.split(" ")
        d, y = int(d), int(y)
        if m in month and 1 <= d <= 31 and y >= 1 :
            n = month.index(m) + 1
            n = int(n)
            print(f"{y:04}-{n:02}-{d:02}")
            break
    except ValueError:
        pass






