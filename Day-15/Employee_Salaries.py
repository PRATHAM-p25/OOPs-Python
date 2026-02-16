class Employee:
    def __init__(self, name, base_salary):
        self.name=name
        self.base_salary=base_salary

class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name,base_salary)
        self.bonus=bonus

    def calculate_salary(self):
        self.base_salary+=self.bonus
        return self.base_salary

d1 = Developer("A", 40000, 5000)
print( d1.calculate_salary())