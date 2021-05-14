class parent:
    def func(self):
        print("this is parent class")
class child(parent):
    
    def func(self):
        
        print("this is child class")
ob=child()
print(ob.func())
