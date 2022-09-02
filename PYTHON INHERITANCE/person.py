person

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f"I am {self.full_name} amd I'm {self.age} years old."

    def age(self):
        return self.__age

    def age(self, value):
        if value <= 0:
            raise ValueError('That age is not valid at all.')

        self.__age = value

    def full_name(self):
        return f"{self.first_name} {self.last_name}"