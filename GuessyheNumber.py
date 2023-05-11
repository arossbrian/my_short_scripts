import random
number = random.randint(0, 20)
# asking player to enter a valu

for numberGuessed in range(1, 6):
    userNumber = int(input("Enter a number between 0 and 20 : "))
    if userNumber < number:
        print("Try a larger value")

    elif userNumber > number:
        print("Enter a lesser value")

    else:
        break #This condition is the correct answer
if userNumber == number:
    print("Good Job")
else:
    print("The number that I weas thinking of was " + str(number))