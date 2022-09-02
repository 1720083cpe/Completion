class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of our Restaurant is {} and our specialties are {}'.format(self.name, self.cuisine_type))

    def open_restaurant(self):
        print('The Restaurant is now officially open!')
        
restaurant = Restaurant('Restawran ni Andeng', 'Lutong Bahay ng Inang Filipino')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()