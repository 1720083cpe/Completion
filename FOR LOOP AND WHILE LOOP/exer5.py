
prompt = "\nWhat toppings would you like to be added in your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        break
    else:
        print (toppings.title() + " will be added to your pizza!")