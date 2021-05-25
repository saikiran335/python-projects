class partyanimal:
    x=0
    def __init__(self):
        print("i am constructed")
    def party(self):
        self.x=self.x+2
        print("so far",self.x)
    def __del__(self):
        print("i am destructed",self.x)
an=partyanimal()
an.party()
an.party()
an=42
print("an contains",an)
