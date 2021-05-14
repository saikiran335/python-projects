class one:
    def func1(self):
        print("this is first function")
class two(one):
    def func2(self):
        print("this is secont function")
class three(one):
    def func3(self):
        print("this is third function")
class four(one):
    def func4(self):
        print("this is fourth function")

ob=two()
ob3=three()
ob4=four()
print(ob.func1())
print(ob3.func1())
print(ob4.func1())
