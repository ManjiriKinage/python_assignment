# Parent class
class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender


# Child class Teacher
class Teacher(Person):
    def teaches(self):
        print("I am a teacher")


# Child class Student
class Student(Person):
    def studies(self):
        print("I study")


# Create objects
t = Teacher(35, "Male")
s = Student(20, "Female")

# Call methods
t.teaches()
s.studies()
