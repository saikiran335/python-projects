class profile:
    age=20
    name=input("enyter name:")
    def __init__(self):
        print("this is my profile")
    def first(self):
        self.name=self.name
        print("my name is:",self.name)
class pro(profile):
    name="kiran"
    def __init__(self):
        print(" started")
    def second(self):
        self.age=self.age
        self.name=self.name
        print("my name is:",self.name)
        print("age:",self.age)
a=pro()
b=profile()
b.first()
a.second()
        
