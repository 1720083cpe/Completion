class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('The name of our Restaurant is {} and our specialties are {}'.format(self.name, self.cuisine_type))

    def open_restaurant(self):
        print('The Restaurant is now officially open!')
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('Restawran ni Andeng', 'Lutong Bahay ng Inang Filipino')

print()
print(restaurant.name)
print(restaurant.cuisine_type)

print("\nTotal served: " + str(restaurant.number_served))

restaurant.number_served = 75
print("Monday Total served: " + str(restaurant.number_served))

restaurant.set_number_served(86)
print("Wednesday Total served: " + str(restaurant.number_served))

restaurant.increment_number_served(84)
print("Friday Total served: " + str(restaurant.number_served))

restaurant.increment_number_served(164)
print("Saturday Total served: " + str(restaurant.number_served))