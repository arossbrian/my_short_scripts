#formula for SI = (P*R*T)/100
#P = Principal Amnt
# R = Rate
#T = Time

#Prompt user for P, R and T
P = float(input("Enter the principle AMnt"))
R = float(input("\nEnter the Rate"))
T = float(input("\nEnter the Time"))

#calculate the SI
SI = (P*R*T)/100
#print("The Principle AMount is " {0} "Rate is "{1} "and the TIme is "{2} " THe simple Interest is" {3} .format(P, R, T, SI))
print(SI)
