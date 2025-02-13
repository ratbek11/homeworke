def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__} с аргументами: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return NotImplemented


# Создаём два прямоугольника
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)

# Складываем их
rect3 = rect1 + rect2

# Вывод результатов
print(rect1)  # Прямоугольник 3x4
print(rect2)  # Прямоугольник 5x6
print(rect3)  # Прямоугольник 8x10
