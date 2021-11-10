def GCD(a, b, PrintMode = False):
    while (b > 0):
        c = a, b = b , a % b
        if(PrintMode == True):
            print(c)
    return a

mode = "none"

while (mode == "none"):
    print("What mode do you want to use?")
    mode = input("LCM or GCD: ")
    if(mode.lower() == "gcd"):
        print("GCD mode activated!")
    elif(mode.lower() == "lcm"):
        print("LCM mode activated!")
    else:
        print("Incorrect answer. Try again! \n")
        mode = "none"

while (mode.lower() == "gcd"):
    try:
        num1 = int(input("Please input the first number of GCD: "))
        num2 = int(input("Please input the second number of GCD: "))
        c = GCD(num1, num2, False)
        print(f"GCD({num1};{num2}) = {c} \n")
    except ValueError:
        print("\nPlease input an integner (only numbers). Do not use strings or booleans. Also it is required\n")

while (mode.lower() == "lcm"):
    try:
        num1 = int(input("Please input the first number of LCM: "))
        num2 = int(input("Please input the second number of LCM: "))
        c = (num1*num2)/GCD(num1, num2)
        print(f"LCM({num1};{num2}) = {c} \n")
    except ValueError:
        print("\nPlease input an integner (only numbers). Do not use strings or booleans. Also it is required\n")
