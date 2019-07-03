#has a function that divide evenly an integer

def factors():
    number = input("Please enter an integer to find its factors : ")
    print("THe number entered is ", str(number))
    for number in range(0, int(number)):
        if (int(number) % 2) == 0:
            print(str(number), "is divisble by 2") 
        elif (int(number) % 2 == 1):
           print(number, " Is not divisble by 2")
    return number
factors()

