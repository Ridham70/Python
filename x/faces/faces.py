def main():
    # Get input from user
    msg = input("Enter symbolized emoji : ")
    #call covert function
    result = convert(msg)
    # Print the result
    print(result)

def convert(msg):
    # Replace :) with happy emoji
    msg1 = msg.replace(":)", "🙂")
    # Replace :( with sad emoji
    msg2 = msg1.replace(":(", "🙁")
    # Return string
    return msg2


main()
