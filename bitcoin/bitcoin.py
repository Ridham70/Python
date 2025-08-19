import sys, requests, json

if len(sys.argv) == 2 :
    try :
        value = float(sys.argv[1])
    except :
        print("Command-line argument is not a number")
        sys.exit(1)
else :
    print("Missing command-line argument")
    sys.exit(1)
try :
    x = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f6f45c2b5fbe975b5b8ee3e5f9b1ddc1262a6cefd0fcf2ee5ca5a34827955db4")
    y = x.json()
    a = y['data']
    b = a["priceUsd"]

    amt = float(b) * value
    print(f"${amt:,.4f}")

except requests.RequestException:
    print("Website not responding.")
