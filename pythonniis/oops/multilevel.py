class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll):
        Person.__init__(self, name, age)
        self.roll = roll

    def display_student(self):
        print("Roll Number:", self.roll)


class EngineeringStudent(Student):
    def __init__(self, name, age, roll, branch):
        Student.__init__(self, name, age, roll)
        self.branch = branch

    def display_engineering(self):
        print("Branch:", self.branch)


# Creating object
e1 = EngineeringStudent("Rahul", 21, 101, "Computer Science")

e1.display_person()
e1.display_student()
e1.display_engineering()
        