age = ''
while True:
    age = int(input("Please enter your age to know how much is your ticket:"))
    if age < 3:
        print("Tickets for people under the age of 3 is free.")
    elif age >=3 and age <= 12:
        print("Tickets for people between the age of 3 and 12 is 10 pesos.")
    else:
        print("Tickets for people above the age of 12 is 15 pesos.")