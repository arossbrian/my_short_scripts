#Accept a name Alice and check if Alice is
#1 Accept Name
#2 Accept Age
#Check if Age <18
#4: Check if age is >2000


def nameChecker():
    name = input("Please enter your name: ")
    age = input("PLease enter your age: ")
    age = int(age)
    if name == "Alice" and age < 30:
        print("Your name is " + name + " and you are " + age + "  years old")
    elif age > 59:
        print("Your age is above 50")

    else:
        print("You are ", name , " and a stranger to us ")

    return nameChecker()
nameChecker()

    

