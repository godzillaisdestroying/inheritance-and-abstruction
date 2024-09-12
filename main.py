class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber= idnumber

    def diplay(self):
        print("Name", self.name, "\nID", self.idnumber) 
  
    
class  Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post



ripley = Employee("Ripley", "2333", 3400 , "space engineer")
ripley.diplay()
