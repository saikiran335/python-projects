class parent:
    def func1(self):
        print("this is parent class")
class child(parent):
    
    def func2(self):
        super().func1()
        print("this is child class")
ob=child()
print(ob.func2())
