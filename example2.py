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

# Create AdaStaff objects
teacher1 = AdaStaff("Alice Johnson", "15/05/1985", "Birmingham", "EMP001", "Education")
admin = AdaStaff("Zara Sharma", "22/09/1979", "Leeds", "EMP002", "Administration")
teacher2=AdaStaff("Vicki Gibbison", "09/04/1980", "Manchester", "EMP003", "SOftware Engineer")
teacher3=AdaStaff("Phil Gibbison", "14/07/1971", "Whithington", "EMP004", "Investment Banker")
# Test the objects
print(teacher3.talk())  # Inherited from Person
print(teacher3.work())  # New method in AdaStaff
print(teacher3.get_employee_info()) 



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



