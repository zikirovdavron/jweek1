#task1
# class Circle:
#     def __init__(self,radius):
#         self.r=radius 

#     def getArea(self):
#         return 3.14*(self.r**2) 

#     def getPerimeter(self):
#         return 2*3.14*self.r 
    
# cr=Circle(11)
# print(cr.getArea())  

# cr=Circle(4.44)
# print(cr.getPerimeter())
# 
#   
#task2
# class Numbers:
#     def __init__(self,number):
#         self.ones=number//1   
#         self.threes=number//3  
#         self.nines=number//9   

# a=Numbers(12)
# print(a.ones)
# print(a.threes)
# print(a.nines)

#task3
# class Player:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight

#     def get_age(self):
#         return f"{self.name} is age {self.age}"

#     def get_height(self):
#         return f"{self.name} is {self.height}cm"

#     def get_weight(self):
#         return f"{self.name} weighs {self.weight}kg"

# p1=Player('Davron',20,162,65)
# print(p1.name)
#task4
# class Employee:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.fullname = f"{firstname} {lastname}"
        # self.email = f"{firstname.lower()}.{lastname.lower()}

#task5
# class User:
#     user_count=0

#     def init(self,username):
#         self.username=username
#         User.user_count+=1
# u1=User("johnsmith")
# print(User.user_count) 
# print(u1.username)      
#task6
class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return f"Title: {self.title}"

    def get_author(self):
        return f"Author: {self.author}"
PP = Book("Margi sudhur", "Sadriddin Aini")