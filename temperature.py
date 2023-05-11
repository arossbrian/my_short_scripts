#1. Must have two functions
"""Function1: takes celsius as input and converts that number
to F and returns that value"""
""" F = C*9/5 + 32
    C = (F -32) * 5/9
"""
import tkinter

def Celsius2F (temp):
       converter = (temp * 9/5)+32
       return converter
input_temp = input("Please enter the Temperature in Celsius to convert to Farenheit: ")
output_temp = Celsius2F(int(input_temp))
print(output_temp)

    
def Farenheight2C(temp2):
    converter = (temp2-32)*5/9
    return converter
input_temp2 = input("Farenheit to Degrees Celsius: ")
output_temp2 = Farenheight2C(int(input_temp2))
print(input_temp2 + " Farenheit to Degrees Celsius is = : " + str(output_temp2))
