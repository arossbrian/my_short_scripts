##This is a multiply function
#takes two figures as inputs and multiples them together

def multiply(num1, num2):
    multiplier = num1 * num2
    return multiplier
input_num1 = input("Please enter the first value: ")
input_num2 = input("Enter the Second Value: ")
##input_num1 = int(input_num1)
##input_num2 = int(input_num2)
Answer = multiply(int(input_num1), int(input_num2))
print(Answer)
