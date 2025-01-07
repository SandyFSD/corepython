# class college:
#     def getStudentInfo(self):
#         self .__rollno=input("Enter Roll number:")
#         self .__name=input("Enter Name:")
        
#     def printStudentInfo(self):
#         print("Roll number:",self.__rollno,"Name:",self.__name)

# class BE(college):
#     def getBE(self):
#         self.getStudentInfo()
#         self.__p=int(input("Enter ur Physics mark:"))
#         self.__c=int(input("Enter ur Chemistry mark:"))
#         self.__m=int(input("Enter ur maths mark:"))

#     def printBE(self):
#         self.printStudentInfo()
#         print("Marks in different subjets:",self.__p,self.__c,self.__m)

#     def calcTotalMarks(self):
#         return(self.__p+self.__c+self.__m)
    
# class Result(BE):
#     def getResult(self):
#         self.getBE()
#         self.__total=self.calcTotalMarks()

#     def putResult(self):
#         self.printBE()
#         print("total marks out of 300:",self.__total)

# college=Result()
# college.getResult()
# college.putResult()