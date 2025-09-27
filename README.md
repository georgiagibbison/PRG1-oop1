# Object-Oriented Programming (OOP) 

## Learning Objectives
By the end of this markdown document, you will be able to:
- Define Class, Object, Constructor, Method, and Attribute (property)
- Create multiple classes with inheritance
- Create at least ten objects from your classes
- Describe the Object-Oriented Programming (OOP) paradigm
- Apply principles of encapsulation using getters and setters

---

## Part 1: Understanding the Basics

### Key Definitions
Firstly, let's understand the fundamental concepts:

**Class**: A blueprint or template for creating objects. Think of it like a cookie cutter - it defines the shape and structure.

**Object**: An individual instance created from a class. Like cookies made from the same cutter - they have the same structure but can have different values.

**Attribute (Property)**: The individual properties or data that an object holds (like name, age, colour).

**Method**: The actions or functions that an object can perform (like talk, walk, calculate).

**Constructor**: A special method (`__init__` in Python) that creates and initialises new objects.

**Instance**: Another term for an object - every new object created from the same class is an instance of that class.

---

## Part 2: Your First Class - Person

Let's start with a simple Person class:

```python
class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self.name} and I was born in {self.place_of_birth}."

# Creating two instances of the Person class
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")

# Using the objects
print(steve.talk())
print(aqil.talk())
print(f"Name: {steve.name}")
print(f"Date of birth: {steve.date_of_birth}")
print(f"Place of birth: {steve.place_of_birth}")

# We can change the name
steve.name = "Stephen Rich"
print(f"Updated name: {steve.name}")
```

### 🤔 Predict Questions (Try before running the code!)
1. What will be printed when we run `print(steve.talk())`?
2. What do you think will be displayed when we execute `print(f"Name: {steve.name}")`?
3. If we run the line `steve.name = "Stephen Rich"`, what will happen to the `steve` object?
4. After creating `aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")`, predict what `aqil.place_of_birth` will contain.

**Now run the code in `example 1.py` and check your predictions!**

---

## Part 3: Encapsulation - Getters and Setters

In good OOP practice, we don't access object attributes directly. Instead, we use **getter** and **setter** methods. This is called **encapsulation** - we control how other parts of our program interact with our objects.

Here's why this matters:
- Some attributes shouldn't be changed (you can't change your date of birth!)
- We can validate data before setting it
- We can control what happens when data is accessed or modified

```python
class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  # Private attribute
        self._date_of_birth = date_of_birth  # Private attribute (read-only)
        self._place_of_birth = place_of_birth  # Private attribute (read-only)
    
    # Getter and setter for name (can be changed)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        self._name = name.strip()
    
    # Getters for immutable attributes (read-only)
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    @property
    def place_of_birth(self):
        return self._place_of_birth
    
    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."
```

**Use the code in `example 2.py` for the following!**

### 🎯 Try This:
1. Create a Person object and try to change the name - it should work
2. Try to set an empty name - what happens?
3. Try to change the date_of_birth - what error do you get?

---

## Part 4: Inheritance - Creating AdaStaff

**Inheritance** allows us to create new classes based on existing ones. The new class inherits all the attributes and methods from the parent class.

```python
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
    ```

# Create AdaStaff objects
teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")

# Test the objects
print(teacher.talk())  # Inherited from Person
print(teacher.work())  # New method in AdaStaff
print(teacher.get_employee_info())
```


**Now copy and paste the code above into `example 2.py` - After L30**

### 🎯 Your Turn:
1. Create 2 more AdaStaff objects with different details
2. Test that they can use both Person methods (like `talk()`) and AdaStaff methods (like `work()`)

---

## Part 5: More Inheritance - Creating AdaStudent

**Now let's create an AdaStudent class that also inherits from Person. Have a read of the code below, and then add it into the `example 2.py` file.**

```python

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

# Test the functionality
print(student1.talk())  # Inherited from Person
print(student1.study())  # New method in AdaStudent

# Add some grades
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

print(student1.get_student_info())

```

### 🎯 Challenge:
Create 4 more AdaStudent objects and give them different courses and grades. Make sure you have at least 6 student objects total.

---

## Part 6: Composition - Creating a Cohort Class

**Composition** is when one class contains objects of another class. Let's create a Cohort class that contains AdaStudent objects:

```python
class Cohort:
    def __init__(self, cohort_code):
        self.cohort_code = cohort_code
        self.students = []  # List to store AdaStudent objects
    
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

# Create a cohort and add students
cohort1 = Cohort("DEV2024A")

# Add our existing students
cohort1.add_student(student1)
cohort1.add_student(student2)

# Create and add more students to reach our goal of 10+ objects
student3 = AdaStudent("Sarah Davis", "25/07/2002", "Liverpool", "STU003", "Software Development")
student4 = AdaStudent("Michael Johnson", "14/12/2001", "Newcastle", "STU004", "Cybersecurity")

cohort1.add_student(student3)
cohort1.add_student(student4)

# Test the cohort functionality
print(cohort1.list_students())

# Add some grades to the new students
student3.add_grade(88)
student3.add_grade(91)
student4.add_grade(76)
student4.add_grade(84)
student4.add_grade(89)

print(f"Cohort average: {cohort1.get_cohort_average():.1f}")
```

### 🎯 Complete the Challenge:
1. Create at least 6 more AdaStudent objects (you should have 10+ total now)
2. Create a second cohort and add some students to it
3. Test removing a student from a cohort
4. Test searching for a student by name

---

## Part 7: Putting It All Together

Now you should have:
- ✅ A Person class (base class)
- ✅ An AdaStaff class (inherits from Person)
- ✅ An AdaStudent class (inherits from Person)  
- ✅ A Cohort class (contains AdaStudent objects)
- ✅ At least 10 objects total
- ✅ Examples of encapsulation, inheritance, and composition

### 🧩 Final Challenge - Matching Exercise
Match the keyword to the definition:

**Keywords:** Class, Object, Method, Attribute, Instance

**Definitions:**
- A. The individual properties of an object
- B. A collection of data and its associated actions
- C. The blueprint for an object
- D. The associated actions of an object
- E. Every new object created from the same blueprint

*(Answers: Class=C, Object=B, Method=D, Attribute=A, Instance=E)*

---

## Part 8: Understanding OOP

**Object-Oriented Programming (OOP)** is a programming paradigm that organises code around objects rather than functions. The key principles are:

1. **Encapsulation**: Bundling data and methods together, controlling access to them
2. **Inheritance**: Creating new classes based on existing ones, promoting code reuse
3. **Polymorphism**: Objects of different types can be used interchangeably
4. **Composition**: Building complex objects by combining simpler ones

### Why Use OOP?
- **Modularity**: Code is organised into logical, reusable units
- **Reusability**: Classes can be reused and extended
- **Maintainability**: Changes to one class don't affect others
- **Real-world modeling**: Objects often represent real-world entities naturally

---

## 🎉 Congratulations!

You've successfully:
- Created multiple classes with inheritance relationships
- Implemented encapsulation with getters and setters
- Used composition to build complex relationships
- Created 10+ objects from your classes
- Learned the fundamental principles of OOP

---

## Summary Checklist
- [ ] I can define Class, Object, Constructor, Method, and Attribute
- [ ] I have created at least 3 classes (Person, AdaStaff, AdaStudent, Cohort)
- [ ] I have created at least 10 objects total
- [ ] I understand inheritance (AdaStaff and AdaStudent inherit from Person)
- [ ] I understand composition (Cohort contains AdaStudent objects)
- [ ] I can explain what Object-Oriented Programming means
- [ ] I understand encapsulation and why we use getters/setters