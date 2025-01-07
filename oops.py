class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def print(self):
        print(self.n,self.c)
        print("Hello")
c=college("MEC",2021)
c.print()

class A:
    def __init__(self,age,place):
        self.A=age;
        self.P=place;
    def display(self):
           print(self.A,self.P)
s=A(20,"MEC")
s.display()