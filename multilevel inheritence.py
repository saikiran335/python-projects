class one:
    def func1(self):
        print("this is first function")
class two(one):
    def func2(self):
        print("this is secont function")
class three(two):
    def func3(self):
        print("this is third function")
class four(three):
    def func4(self):
        print("this is fourth function")
ob=four()
print(ob.func1())
print(ob.func2())
print(ob.func3())
