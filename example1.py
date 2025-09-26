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