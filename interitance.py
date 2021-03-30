class Person:
    def __init__(self,fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    def employee_details(self):
        print("Full name: ", self.firstname,self.lastname)
        print("Age: ",self.age)
        
class employee(Person):
    pass

s = employee("ilyas","Mutlu",19)
s.employee_details()    
