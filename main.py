import math as Math

def GCD(a, b, PrintMode = False):
    while (b > 0):
        c = a, b = b , a % b
        if(PrintMode == True):
            print(c)
    return a

mode = "none"
LeavingModeMessage = "to leave this mode you need to type: CANCEL"

while (mode == "none"):
    modes = ["GCD", "LCM"]
    numbersformode = [1, 2]
    print("What mode do you want to use?")
    for numbersformode,modes in zip(numbersformode, modes):
        print(f'[{numbersformode}] {modes}')
    mode = input("")
    if(mode.lower() == "gcd" or int(mode) == 1):
        mode = "GCD"
        print("GCD mode activated!")
        print(LeavingModeMessage)
    elif(mode.lower() == "lcm" or int(mode) == 2):
        mode = "LCM"
        print("LCM mode activated!")
        print(LeavingModeMessage)
    else:
        print("Incorrect answer. Try again! \n")
        mode = "none"

while (mode.lower() == "gcd"):
    try:
        num1 = input("Please input the first number of GCD: ")
        if(num1 == "CANCEL"):
            mode = "none"
        num2 = input("Please input the second number of GCD: ")
        if(num2 == "CANCEL"):
            mode = "none"

        num1 = float(num1)
        num2 = float(num2)
        
        c = GCD(num1, num2, False)
        print(f"GCD({num1};{num2}) = {c} \n")
    except ValueError:
        print("\nPlease input an integner (only numbers). Do not use strings or booleans. Also it is required\n")

while (mode.lower() == "lcm"):
    try:
        num1 = float(input("Please input the first number of LCM: "))
        num2 = float(input("Please input the second number of LCM: "))
        c = (num1*num2)/GCD(num1, num2)
        print(f"LCM({num1};{num2}) = {c} \n")
    except ValueError:
        print("\nPlease input an integner (only numbers). Do not use strings or booleans. Also it is required\n")
