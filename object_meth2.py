#declaring object usin gdynamic programming
#without using constructors
class Student(object):
    name = ""
    age = 0
    major = ""

def make_student(name,age,major):
    student = Student()
    student.name = name
    student.age = age
    student.major = major

    #if i want to add an extra variable then i dont have to define in this 
    #type of object declaration

    student.gpa = float(4.0)
    return student