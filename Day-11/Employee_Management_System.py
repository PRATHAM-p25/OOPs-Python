class Person:
    def __init__(self, name, emp_id):
        self.name=name
        self.emp_id=emp_id

class Manager(Person):
    def __init__(self, name, emp_id, department):
        super().__init__(name,emp_id)
        self.department=department

    def get_profile_data(self):
        return f'{self.name} (ID: {self.emp_id}) is a manager of {self.department} department.'

class Engineer(Person):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name,emp_id)
        self.specialization=specialization

    def get_profile_data(self):
        if len(self.specialization)>1:
            self.name1= self.specialization[0].lower() + self.specialization[1:]
            return f'{self.name} (ID: {self.emp_id}) is a {self.name1} engineer.'
        else: 
            return f'{self.name} (ID: {self.emp_id}) is a {self.specialization} engineer.'

m1 = Manager("Kavita", 101, "HR")
print( m1.get_profile_data())

e1 = Engineer("Ravi", 102, "Software")
print( e1.get_profile_data())