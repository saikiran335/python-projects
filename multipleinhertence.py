class parent1:
    def func1(self):
        print("this is first function")
class parent2:
    def func2(self):
        print("this is secont function")
class child(parent1,parent2):
    def func3(self):
        print("this is third function")
ob=child()
print(ob.func1())
print(ob.func2())
