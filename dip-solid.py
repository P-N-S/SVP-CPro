# Dependency Inversion Principle (SOLID)
# https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/

# SGVP391900 | 12:03 7Mar19

# Mootto - Any higher classes should always depend upon the abstraction of the class
# rather than the detail.

class Employee(object):
    def Work():
        pass


class Manager():
    def __init__(self):
        self.employees=[]
    def addEmployee(self,a):
        self.employees.append(a)
        # self.developers=[]
        # self.designers=[]
        # self.testers=[]

    # def addDeveloper(self, dev):
    #     self.developers.append(dev)

    # def addDesigners(self, design):
    #     self.designers.append(design)

    # def addTesters(self, testers):
    #     self.testers.append(testers)

    
class Developer(Employee):
    def __init__(self):
        print ("developer added")
    def Work():
        print ("truning coffee into code")

class Designer(Employee):
    def __init__(self):
        print ("designer added")
    def Work():
        print ("turning lines to wireframes")

class Testers(object):
    def __init__(self):
        print ("tester added")

    def Work():
        print ("testing everything out there")


if __name__ == "__main__":
    a=Manager()
    # a.addDeveloper(Developer())
    # a.addDesigners(Designer())
    a.addEmployee(Developer())
    a.addEmployee(Designer())