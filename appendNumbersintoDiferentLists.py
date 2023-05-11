#This program accepts numbers and adds even numbers to a list and odd numbers to a separate list

#1.Create an empty list for odd and even numbers

a = []
n = int(input("Enter number of elements"))
for i in range(1, n+1):
    b = int(input("Enter Element: "))
    a.append(b)

odd_no = []
even_no = []
for j in a:
    if (j%2 == 0):
        even_no.append(j)
    else:
        odd_no.append(j)
print("The odd numbers are ",  odd_no )
print("The odd numbers are ",  even_no)


#Promt user to input numbers


