full_name = 'guest_book.csv'
print("\n****WELCOME TO QWERTY RESORT****\n")
print("\n****THIS IS OUR GUESTBOOK. PLEASE SRRICTLY FOLLOW THE INSTRUCTIONS. THANK YOU!****\n")
print("\n****EVERYTHING YOU INPUT WILL BE RECORDED IN OUR GUEST BOOK.****\n")
print("\n****Please enter 'exit' once you are done! Thank you!****\n")

while True:
    name = input("\nName: ")
    date = input("(Year/Month/Date): ")
    if name == 'exit':
        break
    else:
        with open(full_name, 'a') as f:
            f.write(name + "\n")
            f.write(date + "\n")
            print("\n****GREETINGS!" + name + ", YOU HAVE BEEN SUCCESSFULLY ADDED AT OUR GUEST BOOK.****\n")
            print("\n****YOU'VE BEEN BOOKED AT " + date + ". PLEASE ENJOY YOUR STAY!****\n")
            print("\n****THANK YOU AND HAVE A GREAT DAY!****\n")