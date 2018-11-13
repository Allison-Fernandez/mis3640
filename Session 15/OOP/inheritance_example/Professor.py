from BabsonPerson import BabsonPerson
from Person import Person

class Professor(BabsonPerson):

    def __init__(self, name, department):
        BabsonPerson.__init__(self, name)
        self.department = department
    
    def getDept(self):
        return self.department

    def teach(slef, subject):
        return BabsonPerson.grade(self, "I teach: " + subject)

