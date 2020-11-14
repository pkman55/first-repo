small = None
big = None

while(True):
    inp = input("Please enter a number ")
    try:
        sk = int(inp)
        if small is None:
            small = sk
        if big is None:
            big = sk

        if big < sk:
            big = sk
        if small > sk:
            small = sk

    except:
        print("Invalid input ")
        if inp == "done":
            break

print("Maximum is", big)
print("Minimum is", small)
