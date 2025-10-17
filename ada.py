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