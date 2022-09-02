class User:
    def __init__(self, first_name, last_name, age, sex, location):
        self.first_name = first_name.title() 
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.location = location.title()
    def describe_user(self):
        print('{} {} is {} years old, {} from {}'.format(self.first_name, self.last_name, self.age, self.sex, self.location))

    def greet_user(self):
        print('Good Day! {}, welcome to CPE2A!\n'.format(self.first_name))


# User A

name = User('Roman', 'Librada', 20, 'male', 'Lipa City, Batangas')

print(name.first_name)
print(name.last_name)
print(name.age)
print(name.sex)
print(name.location)
print()

name.describe_user()
print()

name.greet_user()
print()

# User B
name1 = User('Andrea', 'Olan', 20, 'Female', 'Lipa City, Batangas')
print(name1.first_name)
print(name1.last_name)
print(name1.age)
print(name1.sex)
print(name1.location)
print()

name1.describe_user()
print()

name1.greet_user()
print()

# User 3
name2 = User('Althea', 'Sabando', 21, 'Female', 'Tanauan City, Batangas')
print(name2.first_name)
print(name2.last_name)
print(name2.age)
print(name2.sex)
print(name2.location)
print()

name2.describe_user()
print()

name2.greet_user()
print()