from Employee import Employee

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def introduce(self):
        return f"I am {self.full_name} and my total salary is Php{self.salary}."    

fulltimeemployee1 = FulltimeEmployee('Andrea', 'Olan', 245000)
fulltimeemployee2 = FulltimeEmployee('Althea', 'Ranes', 245000)

print()
print(fulltimeemployee1.introduce())
print()
print(fulltimeemployee2.introduce())
print()