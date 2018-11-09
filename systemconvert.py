def promptDecimal():
    # store user's input temporarily as string to concatenate later
    tmp = input("[decimal input] > ")
    userDecimal = int(tmp)
    print("""
            [1] to binary
            [2] to hex
            [r] reset
            """)
    targetSystem = input("[target system] > ")
    if targetSystem == "1":
        print(tmp + " in binary: " + str(bin(userDecimal)[2:]))
    elif targetSystem == "2":
        print(tmp + " in hex: " + str(hex(userDecimal)[2:]))
    elif targetSystem == "r":
        userMenu()

def promptBinary():
    # store user's input temporarily as string to concatenate later
    tmp = input("[binary input] > ")
    # convert binary string to decimal int by using base (2) as parameter
    userBinary = int(tmp, 2)
    print("""
            [1] to decimal
            [2] to hex
            [r] reset
            """)
    targetSystem = input("[target system] > ")
    if targetSystem == "1":
        print(tmp + " in decimal: " + str(userBinary))
    elif targetSystem == "2":
        print(tmp + " in hex: " + str(hex(userBinary))[2:])
    elif targetSystem == "r":
        userMenu()

def promptHex():
    # store user's input temporarily as string to concatenate later
    tmp = input("[hex input] > ")
    # convert hex string to decimal int by using base (16) as parameter
    userHex = int(tmp, 16)
    print("""
            [1] to decimal
            [2] to binary
            [r] reset
            """)
    targetSystem = input("[target system] > ")
    if targetSystem == "1":
        print(tmp + " in decimal: " + str(userHex))
    elif targetSystem == "2":
        print(tmp + " in binary: " + str(bin(userHex)[2:]))
    elif targetSystem == "r":
        userMenu()

def userMenu():
    print("""
            ----------------------------------------------
            | \t systemconvert.py \t\t\t |
            | \t created by: felix kalg, kevin mai \t |
            | \t version 0.1.0 \t\t\t\t |
            ----------------------------------------------
        """)
    print("""
            [1] - decimal input
            [2] - binary input
            [3] - hex input
            [q] - exit program
          """)
    userChoice = ""
    while userChoice != "q":
        userChoice = input("[input system] > ")
        if userChoice == "1":
            promptDecimal()
        elif userChoice == "2":
            promptBinary()
        elif userChoice == "3":
            promptHex()
        break

userMenu()
