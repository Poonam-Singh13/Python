# class Employee:
#     def info(self,name,age,country):
#         self.name=name
#         self.age=age
#         self.country=country
#         return f"name: {self.name} \n age: {self.age}\n country: {self.country}"
# e1=Employee()
# print(e1.info("poonam",20,"India"))
# print(e1.info("prabhat",25,"US"))

# class University:
#     def __init__(self,uniName,uniCode):
#         self.uniName=uniName
#         self.uniCode=uniCode
#         print(f"this is {self.uniName} university with code {self.uniCode}")
# class Teacher(University):
#     def __init__(self,uniName,uniCode,tName,tSub):
#         super().__init__(uniName,uniCode)
#         self.tName=tName
#         self.tSub=tSub
#         print(f"the teacher name is{self.tName} under {self.uniName} and teaches {self.tSub}")

# t=Teacher("RGPV",205,"Shyam","Machine learning")

# class TwoDVec:
#     def func1(self,i, j):
#         self.i=i
#         self.j=j
#     def Show(self):
#         print(f"{self.i}i , {self.j}j")
# class ThreeDVec(TwoDVec):
#     def func2(self,i,j,k):
#         super().func1(i,j)
#         self.k=k
#     def Show(self):
#         print(f"{self.i}i , {self.j}j , {self.k}k")

# a=ThreeDVec()
# a.func2(1,2,3)
# a.Show()

class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,com):
         return Complex(self.r + com.r, self.i + com.i)
    def __sub__(self,com):
        return Complex(self.r-com.r,self.i-com.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"
 
c1 = Complex(3, 2)
c2 = Complex(1, 7)
c3 = c1 + c2 
c4 = c1-c2
print(c3)
print(c4)    

        

        
   
    