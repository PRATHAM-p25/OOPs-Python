class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Faculty(Person):
    def __init__(self, subject, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject

    def teach(self):
        pass


class Staff(Person):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def work(self):
        pass


class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        super().__init__(name=name, subject=subject, department=department)

    def profile_data(self):
        return f'{self.name} teaches {self.subject} and works in {self.department} department.'


a1 = Administrator("Rakesh", "Math", "Operations")
print(a1.profile_data())
