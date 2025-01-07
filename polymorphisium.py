#POLYMORPHISM
# class Bird:
#     def sound(self):
#         print("CUCKKOO")

#     def fly(self):
#         print("its can be flying the birds")
# class Bird1(Bird):
#     def cockatail(self):
#         print("cuteiee")
# class Bird2(Bird):
#     def Lovebirds(self):
#         print("couple of love")
# obj1=Bird()
# obj2=Bird1()
# obj3=Bird2()
# obj1.sound()
# obj1.fly();
# obj1.sound()
# obj2.cockatail()
# obj1.sound()
# obj3.Lovebirds()

#overloading
# class sam:
#     def aa(self,a):
#         print(a)
#     def aa(self,a,b):
#         print(a+b)
#     def aa(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.aa(10)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# o=over()

# print("Sum",o.load(10))
# print("sum1",o.load(10,20)) 
# print("sum",o.load(10,20,30))


#multiple args passing 
# class multiple:
#     def add(self,*args):
#         sum=40;
#         for i in args:
#             sum+=i
            
#         print("add values:",sum)
            
# m=multiple()
# #m.add(20)
# m.add(40,50)
# m.add(40,50,100)
# m.add(40,50,100,200)
# m.add(10,20,60,100,150)
# m.add(10,20,30,40,50,60,70)

#OVERRIDING
# class sam:
#     def name(self):
#         print("sampk")
# class raja(sam):
#     def name(self):
#         super().name()
#         print("raja")
# class arun(raja):
#     def name(self):
#         super().name()
#         print("ARUN")
# # s=arun()
# # s.name()
# # s1=raja()
# # s1.name()
# s=arun()
# s.name()