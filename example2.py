#parent class
#constructor?
class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth
        self._place_of_birth = place_of_birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.strip()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def place_of_birth(self):
        return self._place_of_birth

    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."

#inheritance
class AdaStaff(Person):
    def __init__(self, name, date_of_birth, place_of_birth, employee_id, department):
        super().__init__(name, date_of_birth, place_of_birth)
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

#inheritance
class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, student_id, course):
        super().__init__(name, date_of_birth, place_of_birth)
        self._student_id = student_id
        self._course = course
        self._grades = []

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

#composition
class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self.students = []

    def add_student(self, student):
        if isinstance(student, AdaStudent):
            self.students.append(student)
            print(f"Added {student.name} to {self.cohort_code}")
        else:
            print("Can only add AdaStudent objects to cohort")

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Removed {student_name} from {self.cohort_code}")
                return
        print(f"Student {student_name} not found in {self.cohort_code}")

    def list_students(self):
        if not self.students:
            return f"No students in {self.cohort_code}"

        result = f"Students in {self.cohort_code}:\n"
        for student in self.students:
            result += f"- {student.name} ({student.course})\n"
        return result

    def search_student(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                return student
        return None

    def get_cohort_average(self):
        if not self.students:
            return 0

        total_average = 0
        students_with_grades = 0

        for student in self.students:
            avg = student.get_average_grade()
            if avg > 0:
                total_average += avg
                students_with_grades += 1

        return total_average / students_with_grades if students_with_grades > 0 else 0


cohort1 = Cohort("DEV2024A")
cohort2=Cohort("COH2025AB")

student1 = AdaStudent("Emma Wilson", "12/03/2002", "Manchester", "STU001", "Software Development")
student2 = AdaStudent("James Brown", "08/11/2001", "London", "STU002", "Data Science")
student3 = AdaStudent("Georgia Gibbison", "20/11/2006", "Cheadle", "STU003", "CyberSecurity")
student4 = AdaStudent("Gracie-Lea Gibbison", "16/06/2008", "Stockport", "STU004", "Media Studies")
student5 = AdaStudent("Vicki Gibbison", "09/04/1980", "Manchester", "STU005", "Computer Science")
student6 = AdaStudent("Phil Gibbison", "14/07/1971", "Whithington", "STU006", "Investment Banking")
student7 = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU007", "Software Development")
student8 = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU008", "Cybersecurity")
student9 = AdaStudent("Liam Thompson", "03/05/2003", "Sheffield", "STU009", "Data Analytics")
student10 = AdaStudent("Chloe Patel", "17/08/2002", "Leicester", "STU010", "Software Engineering")
student11 = AdaStudent("Ethan Wright", "22/01/2000", "Bristol", "STU011", "Artificial Intelligence")
student12 = AdaStudent("Isla Robinson", "09/09/2004", "York", "STU012", "Digital Marketing")
student13 = AdaStudent("Noah Green", "30/06/2001", "Cambridge", "STU013", "Cybersecurity")
student14 = AdaStudent("Freya Ahmed", "14/02/2005", "Oxford", "STU014", "Game Development")
student15 = AdaStudent("Oscar Lewis", "26/11/2003", "Norwich", "STU015", "Cloud Computing")
student16 = AdaStudent("Grace Hall", "05/07/2002", "Bath", "STU016", "UX/UI Design")


cohort1.add_student(student1)
cohort1.add_student(student2)
cohort1.add_student(student3)
cohort1.add_student(student4)
cohort1.add_student(student5)
cohort1.add_student(student6)
cohort1.add_student(student7)
cohort1.add_student(student8)
cohort2.add_student(student9)
cohort2.add_student(student10)
cohort2.add_student(student11)
cohort2.add_student(student12)
cohort2.add_student(student13)
cohort2.add_student(student14)
cohort2.add_student(student15)
cohort2.add_student(student16)


print(cohort1.list_students())

student7.add_grade(88)
student7.add_grade(91)
student8.add_grade(76)
student8.add_grade(84)
student8.add_grade(89)
student9.add_grade(72)

student9.add_grade(85)
student9.add_grade(90)

student10.add_grade(88)
student10.add_grade(79)

student11.add_grade(91)
student11.add_grade(87)
student11.add_grade(93)

student12.add_grade(76)
student12.add_grade(82)

student13.add_grade(84)
student13.add_grade(89)
student13.add_grade(78)

student14.add_grade(95)
student14.add_grade(88)

student15.add_grade(80)
student15.add_grade(85)
student15.add_grade(77)

student16.add_grade(90)
student16.add_grade(86)


print(f"Cohort average: {cohort1.get_cohort_average():.1f}")
print(f"Cohort average: {cohort2.get_cohort_average():.1f}")
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
print(student9.get_student_info())
print(student10.get_student_info())
print(student11.get_student_info())
print(student12.get_student_info())
print(student13.get_student_info())
print(student14.get_student_info())
print(student15.get_student_info())
print(student16.get_student_info())


teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")
teacher2 = AdaStaff("Vicki Gibbison", "09/04/1980", "Manchester", "EMP003", "Software Engineer")
teacher3 = AdaStaff("Phil Gibbison", "14/07/1971", "Whithington", "EMP004", "Investment Banker")

print(teacher3.talk())
print(teacher3.work())
print(teacher3.get_employee_info())

aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")
olivia = Person("Olivia Edet", "11/01/2007", "Scotland")

print(steve.talk())
print(f"Name: {steve.name}")
print(f"Date of birth: {steve.date_of_birth}")
print(f"Place of birth: {steve.place_of_birth}")
print(steve.talk())

steve.name = "Stephen Rich"
print(f"Updated name: {steve.name}")
