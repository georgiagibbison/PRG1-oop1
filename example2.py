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
    
    @name.setter
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
    
# Creating instances
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = Person("Steve Rich", "06/06/1998", "London")

# Accessing properties through getters
print(steve.talk())
print(f"Name: {steve.name}")
print(f"Date of birth: {steve.date_of_birth}")
print(f"Place of birth: {steve.place_of_birth}")

# We can change the name (has a setter)
steve.name = "Stephen Rich"
print(f"Updated name: {steve.name}")

# But we cannot change date_of_birth or place_of_birth (no setters)
# These would raise AttributeError:
# steve.date_of_birth = "07/07/1999"  # This would fail!
# steve.place_of_birth = "Birmingham"  # This would fail!
