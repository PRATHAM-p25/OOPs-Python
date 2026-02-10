class Student:
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-------------------")

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Aegon", 101)
s2 = Student("Duncan", 102)

s1.display()
s2.display()

Student.change_college("XYZ Engineering College")

s1.display()
s2.display()

print("Aegon Result:", Student.is_pass(78))
print("Duncan Result:", Student.is_pass(30))
