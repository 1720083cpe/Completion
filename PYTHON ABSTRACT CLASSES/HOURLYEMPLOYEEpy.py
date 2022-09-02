from Employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate

    def introduce(self):
        return f"I am {self.full_name} and the total hours I have worked is {self.worked_hours} for one year and I earned Php{self.rate} per hour during this year."        

hourlyemployee1 = HourlyEmployee('Andrea','Olan',2021, 790)
hourlyemployee2 = HourlyEmployee('Althea','Ranes',1902, 776)
hourlyemployee3 = HourlyEmployee('Gabriel','Hajas', 2350, 720)    

print(hourlyemployee1.introduce())
print()
print(hourlyemployee2.introduce())
print()
print(hourlyemployee3.introduce())
print()