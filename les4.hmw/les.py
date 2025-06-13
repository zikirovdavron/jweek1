# 1. Транспорт
# Создай класс Transport:
# Атрибуты: name, speed
# Метод: show_info() — выводит имя и скорость транспорта
# Создай подкласс Car, который:
# Наследует Transport
# Добавляет атрибут fuel_type
# Переопределяет метод show_info(), чтобы он также выводил fuel_type
# class Transport:
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed

#     def show_info(self):
#         print(self.name,self.speed)
# class Car(Transport):
#     def __init__(self, name, speed,fuel_type):
#         super().__init__(name, speed)
#         self.fuel_type=fuel_type
#     def getall(self):
#         print(self.name)
#         print(self.speed)
#         print(self.fuel_type)


# Cr=Car('Mersedes','320km','Diesel')
# Cr.getall()



# ✅ 2. Человек и студент
# Создай класс Person:
# Атрибуты: name, age
# Метод: introduce() — выводит Привет, меня зовут {name}
# Создай подкласс Student, который:
# Добавляет атрибут university
# Добавляет метод study(), который выводит Я учусь в {university}
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def introduce(self):
#         print(f'Hello my name is {self.name}')
# class Student(Person):
#     def __init__(self, name, age,university):
#         super().__init__(name, age)
#         self.university=university
#     def  study(self):
#         print(f'I study {self.university}')

# pr=Person('Davron','23')
# pr.introduce()
# st=Student('Davron','23','Dmt')
# st.study()




# ✅ 3. Животные
# Создай класс Animal:
# Атрибут: name
# Метод: speak() — выводит Животное издает звук
# Создай подкласс Cat, который:
# Переопределяет метод speak() так, чтобы он выводил Мяу
# class Animal:
#     def __init__(self,name):
#         self.name=name
    
#     def speak(self):
#         print('hrr')

# class Cat(Animal):
#     def speak(self):
#         print('Myau')

# an=Animal('Dog')
# an.speak()
# ct=Cat('Dog')
# ct.speak()
        




# ✅ 4. Фигуры
# Создай базовый класс Shape:
# Метод: area() — возвращает 0
# Создай два подкласса:
# Circle — принимает радиус, реализует area() как π * r²
# Rectangle — принимает ширину и высоту, реализует area() как width * height
# class Shape:
#     def area(self):
#         return 0
# class Circle(Shape):
#     def __init__(self,r):
#         super().__init__()
#         self.r=r
#     def rad(self):
#         s=(3.14)*(self.r**2)
#         return s
# class Rectangle(Shape):
#     def __init__(self,a,b):
#         super().__init__()
#         self.a=a
#         self.b=b
#     def p(self):
#         l=self.a*self.b
#         return l
# sh=Shape()
# cir=Circle(2)
# print(cir.rad())
# rc=Rectangle(2,4)
# print(rc.p())

# ✅ 5. Сотрудники
# Создай класс Employee:
# Атрибуты: name, salary
# Метод: get_salary() — возвращает зарплату
# Создай подкласс Manager, который:
# Добавляет атрибут bonus
# Переопределяет get_salary() — возвращает salary + bonus
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def get_salary(self):
#         return self.salary
# class Manager(Employee):
#     def __init__(self, name, salary,bonus):
#         super().__init__(name, salary)
#         self.bonus=bonus
#     def get_salary(self):
#         return super().get_salary()+self.bonus
    
# mn=Manager('Davron',25,2)
# print(mn.get_salary())
    
        