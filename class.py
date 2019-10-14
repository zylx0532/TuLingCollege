

class Ruixin():
    name="NoName"
    now=0
    def __init__(self,name,now):
        self.name=name
        self.now=now
    def pr(self):
        print("Name:{},Now:{}".format(self.name,self.now))

r1=Ruixin("11111",11)
r2=Ruixin("22222",22)
print(id(r1))
r1.pr()
print(id(r2))
r2.pr()
r1,r2=r2,r1
print(id(r1))
r1.pr()
print(id(r2))
r2.pr()