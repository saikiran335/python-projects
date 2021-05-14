class employee():
    def __init__(self,name,empid,salary,contact):
        self.name=name
        self.empid=empid
        self.salary=salary
        self.contact=contact

emp1=employee("sai",12345,1000000,987654321)
emp2=employee("kiran",12346,2000000,987654322)

print(emp1.__dict__)
print(emp2.__dict__)
