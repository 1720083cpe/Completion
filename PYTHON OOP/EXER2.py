class User():

    def __init__(self, first_name, last_name, age, sex, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.location = location.title()
        self.login_attempts = 0 

    def describe_user(self):
        print('His/Her name is {} {} and he/she is {} years old, {} and from {}'.format(self.first_name, self.last_name, self.age, self.sex, self.location))
        
    def greet_user(self):
       print('Good Day! {}, we would like to tell that you are now a part of CPE2A!\n'.format(self.first_name))
    
    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0

# User A
print('\nUser A:')
name = User('Roman', 'Librada', 20, 'male', 'Lipa City, Batangas')
name.describe_user()
name.greet_user()

# User 2
print('\nUser B:')
name1 = User('Andrea', 'Olan', 20, 'Female', 'Lipa City, Batangas')
name1.describe_user()
name1.greet_user()

# User C
print('\nUser C:')
name2 = User('Althea', 'Sabando', 21, 'Female', 'Tanauan City, Batangas')
name2.describe_user()
name2.greet_user()

print("\nMaking multiple login attempts...")
name.increment_login_attempts()
name1.increment_login_attempts()
name1.increment_login_attempts()
name.increment_login_attempts()
name2.increment_login_attempts()
name1.increment_login_attempts()
name2.increment_login_attempts()
name.increment_login_attempts()

print("  {User 1} Login attempts: " + str(name.login_attempts))
print("  {User 2} Login attempts: " + str(name1.login_attempts))
print("  {User 3} Login attempts: " + str(name2.login_attempts))