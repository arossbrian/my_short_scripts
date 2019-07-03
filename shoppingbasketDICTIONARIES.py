print ("""
Shopping Basket OPtions
---------------------------
1: Add item
2: Remove item
3: View basket
0: Exit Program

""")
shopping_basket = {}
option = int(input("Enter an Option: "))
while option != 0:
    if option == 1:
        item = input("Add an Item :")
        qnty = int(input("Enter the quantity: "))
               for item, qnty in shopping_basket.items():
                print(item)
        #print(shopping_basket)
    #elif option == 2:
        
    
