#this script prompts the user for input

typePassword = input("Tell me your password ")
#print(typePassword)
#Determine the first letter of the user's input
firstLetterOfPassword = typePassword[0]
upperCaseFirst = firstLetterOfPassword.upper()
print("The First Letter of Your Password was", upperCaseFirst)

