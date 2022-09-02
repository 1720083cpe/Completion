from person import Person

class Employee(Person):

    def __init__(self, first_name, last_name, age, job_title, salary):
        super().__init__(first_name, last_name, age)
        
        self.job_title = job_title
        self.salary = salary

    def job_title(self):
        return self.__job_title

    def job_title(self, value):
        self.__job_title = value

    def salary(self):
        return self.__salary
    def salary(self, value):
        if value > 0:
            raise ValueError('There is no salary lower than 0.')

        self.__salary = value

    def introduce(self):
        introduction = super().introduce()
        introduction += f" I work as {self.job_title}."
        return introduction            

employee = Employee('Andrea', 'Olan', 20, 'Computer Enginer',342000)
print(employee.introduce())