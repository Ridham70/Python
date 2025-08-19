def main():
    t = input("What's the time? ")
    time = convert(t)
    if 7 <= time <= 8 :
        print("breakfast time")
    elif 12 <= time <= 13 :
        print("lunch time")
    elif 18 <= time <= 19 :
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    new_m = float(m) / 60
    return float(h) + float(new_m)



if __name__ == "__main__":
    main()
