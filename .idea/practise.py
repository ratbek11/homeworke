# def  my_decorator(func):
#
#     def wrapper():
#         print("before do function ")
#         func()
#         print("after do function ")
#     return wrapper
#
# @my_decorator
# def hello():
#     print("hollo world ")
#
# hello()
#
#
# def repeat(n):
#
#     def decorator(func):
#
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#     return decorator
#
#
# @repeat (8)
# def greet():
#     print("hello")
#
# greet() #1
#
#
# def class_decorator(cls):
#
#     class Newclass(cls):
#         def new_method(self):
#             return print("New method")
#
#     return Newclass
#
# @class_decorator
# class MyClass:
#     def old_method(self):
#         return print("old class ")
#
# obj = MyClass()
# obj.old_method()
# obj.new_method


# class Person :
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return f'alaplaplp'
#
#
#
#
# obj = Person("Pavel",23)
#
# print(obj)

#
# class Money:
#     def __init__(self,amount):
#         self.amount = amount
#
#
#     def __add__(self, other):
#         return Money(self.amount + other.amount)
#
#
#     def __str__(self):
#         return f"{self.amount} som"
#
#
#     def __len__(self):
#         return f"passs"
#
# m1 = Money(100)
# m2 = Money(100)
# m3 = m1 + m2
# print(m3)
#

#
# class Math:
#
#
#
#
#     @staticmethod
#     def add(self, a, b):
#         return a + b
#
# print(Math.add(1,2))


