# 1 TASK
class Person:
    def __init__(self):
        self._age = 0  # Приватный атрибут

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Ошибка: возраст не может быть отрицательным!")

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Ошибка

# 2 TASK

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Rex")
cat = Cat("Mercy")

print(dog.name, dog.speak())
print(cat.name, cat.speak())


# 3 TASK

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling


# 4 task

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

# Пример использования
rect = Rectangle(12, 7)
circle = Circle(7)

print(f"Rectangle area: {rect.area()}")  # Вывод: Rectangle area: 84
print(f"Circle area: {circle.area():.2f}")  # Вывод: Circle area: 153.94
