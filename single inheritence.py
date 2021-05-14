class parent:
    def func1(self):
        print("this is parent class")
class child(parent):
    def func2(self):
        print("this is child class")
ob=child()
print(ob.func1())
