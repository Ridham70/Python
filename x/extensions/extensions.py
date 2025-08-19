y = input("File name: ").lower().strip()

if "gif" in y :
    print("image/gif")
elif "jpg" in y :
    print("image/jpeg")
elif "jpeg" in y :
    print("image/jpeg")
elif "png" in y :
    print("image/png")
elif "pdf" in y :
    print("application/pdf")
elif "txt" in y :
    print("text/plain")
elif "zip" in y :
    print("application/zip")
else :
    print("application/octet-stream")
