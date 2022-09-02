print ("\n\n****HELLO!****\n")

StudentInfo = {}

student_name = input("Enter student's name: ")

student_ID =  input("Enter student's ID (Make sure to follow the naming convention plus the last 3 digits of your student ID!): ")

YNC = input("Enter student's year and course: ")

IWV = input("Enter student's initial wallet value: ")

StudentInfo[student_name] = student_ID
StudentInfo[YNC] = IWV

print ("\n\n****STUDENT DATA****\n")

print("Name: " +student_name)
print("ID: " + student_ID)
print("Year and Course: " + YNC)
print("Balance: Php" + IWV)

print("\n\n****WELCOME TO THE CANTEEN****\n")


print("\n\n****FOOD MENU****\n")

print("\n\n****DRINKS****\n")

print("Soda-------------Php 29.25------Quantity: 4")
print("Bottled Water----Php 20.00------Quantity: 4")
print("Coffee-----------Php 50.00------Quantity: 2")
print("Tea--------------Php 35.50------Quantity: 2")

print("\n\n****SNACKS****\n")

print("Bread------------Php 15.00------Quantity: 1")
print("Apple------------Php 20.50------Quantity: 5")
print("Banana-----------Php 15.00------Quantity: 5")
print("Oranges----------Php 25.10------Quantity: 3")

print("\n\n****MEALS****\n")

print("Tapsilog---------Php 80.99------Quantity: 5")
print("Porksilog--------Php 80.99------Quantity: 4")

print ("\n\n****ORDER****\n")

item = str(input("What item would you like to purchase? (Please enter the item name correctly!): "))

if item == "soda":
    balance = float(IWV) - 29.25
    print("\nSoda purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "bottled water":
    balance = float(IWV) - 20.00
    print("\nBottled Water purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "coffee":
    balance = float(IWV) - 50.00
    print("\nCoffee purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "tea":
    balance = float(IWV) - 35.50
    print("\nTea purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "bread":
    balance = float(IWV) - 15.00
    print("\nBread purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "apple":
    balance = float(IWV) - 20.50
    print("\nApple purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "banana":
    balance = float(IWV) - 15.00
    print("\nBanana purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "orange":
    balance = float(IWV) - 25.10
    print("\nOrange purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "tapsilog":
    balance = float(IWV) - 80.99
    print("\nTapsilog purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
elif item == "porksilog":
    balance = float(IWV) - 80.99
    print("\nPorksilog purchased successfully! Your remaining balance is " + str(balance) + ".\n")
    
else:
    
    print ("\n\n****ENTER THE CORRECT ITEM NAME****\n")
    
print("\n\n****THANK YOU FOR PURCHASING AT THE CANTEEN!****\n")

print("\n\n****PLEASE COME AGAIN****\n")
