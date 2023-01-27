class Student:
    pass
class Marks:
    pass
student_1 = Student()
marks_1 = Marks()

print(isinstance(student_1, Student))
print(isinstance(marks_1, Student))
print(isinstance(marks_1, Marks)) 
print(isinstance(student_1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 