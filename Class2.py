class Employee():
    def s1(self, ename, eid):
        self.ename = ename
        self.eid = eid
    def displayEmployee(self):
        print(f"id : {self.eid} name:{self.ename}")
class Department():
    def s2(self,dname,did):
        self.dname = dname
        self.did = did
    def displayDept(self):
        print(f"dept id : {self.did} dept name:{self.dname}")
class admin(Employee,Department):
    def __init__(self):
        self.name="Admin"


a=admin()
a.s1("Raziq khan",55797)
a.s2("ECE",112)
a.displayEmployee()
a.displayDept()