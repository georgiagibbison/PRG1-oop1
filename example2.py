# Version 2

class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute with getter/setter
        self._date_of_birth = date_of_birth  # Private attribute, read-only
        self._place_of_birth = place_of_birth  # Private attribute, read-only
    
    # Properties for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter #cannot be changed
    def name(self, name):
        self._name = name.strip()
    
    # Properties for date_of_birth (read-only - you can't change when you were born!)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    # Properties for place_of_birth (read-only - you can't change where you were born!)
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."

class AdaStaff(Person):  # AdaStaff inherits from Person
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)  # Call parent constructor
        self._employee_id = employee_id
        self._department = department

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    def work(self):
        return f"{self.name} is working in the {self.department} department."

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"


class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []  # Private list to store grades

    @property
    def student_id(self):
        return self._student_id

    @property
    def course(self):
        return self._course

    @property
    def grades(self):
        return self._grades

    def study(self):
        return f"{self.name} is studying {self.course}."

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self._grades.append(grade)
        else:
            print("Grade must be between 0 and 100")

    def get_average_grade(self):
        if self._grades:
            return sum(self._grades) / len(self._grades)
        return 0

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Course: {self.course}, Average: {self.get_average_grade():.1f}"

# Create AdaStudent objects
student1 = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
student2 = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
student3=AdaStudent("Georgia Gibbison", "20/11/2006","Cheadle", "STU003", "CyberSecurity")
student4=AdaStudent("Gracie-Lea Gibbison","16/06/2008", "Stockport", "STU004", "Media Studies")
student5=AdaStudent("Vicki Gibbison", "09/04/1980", "Manchester", "STU005", "Computer Science")
student6=AdaStudent("Phil Gibbison", "14/07/1971", "Whithington", "STU006", "Investment Banking")

# Test the functionality
print(student1.talk())  # Inherited from Person
print(student1.study())  # New method in AdaStudent

# Add some grades
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(84)
student2.add_grade(20)
student2.add_grade(58)

student3.add_grade(89)
student3.add_grade(62)
student3.add_grade(75)

student4.add_grade(95)
student4.add_grade(42)
student4.add_grade(68)

student5.add_grade(53)
student5.add_grade(71)
student5.add_grade(32)

student6.add_grade(78)
student6.add_grade(62)
student6.add_grade(48)

print(student1.get_student_info())
print(student2.get_student_info())
print(student3.get_student_info())
print(student4.get_student_info())
print(student5.get_student_info())
print(student6.get_student_info())

# # Create AdaStaff objects
# teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
# admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")
# teacher2=AdaStaff("Vicki Gibbison", "09/04/1980", "Manchester", "EMP003", "SOftware Engineer")
# teacher3=AdaStaff("Phil Gibbison", "14/07/1971", "Whithington", "EMP004", "Investment Banker")
# # Test the objects
# print(teacher3.talk())  # Inherited from Person
# print(teacher3.work())  # New method in AdaStaff
# print(teacher3.get_employee_info()) 



# Creating instances
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")
olivia=Person("Olivia Edet", "11/01/2007", "Scotland")

# Accessing properties through getters
# print(steve.talk())
# print(f"Name: {steve.name}")
# print(f"Date of birth: {steve.date_of_birth}")
# print(f"Place of birth: {steve.place_of_birth}")
# print(steve.talk())

# We can change the name (has a setter)
# steve.name = "Stephen Rich"
# print(f"Updated name: {steve.name}")

# But we cannot change date_of_birth or place_of_birth (no setters)
# These would raise AttributeError:
#steve.date_of_birth = "07/07/1999"  # This would fail!
# steve.place_of_birth = "Birmingham"  # This would fail!



