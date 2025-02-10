# Определение базового класса Figure
class Figure:
    # Атрибут уровня класса для единицы измерения
    unit = "cm"  # Единица измерения по умолчанию

    def __init__(self):
        pass  # В этом классе нет атрибутов уровня объекта

    def calculate_area(self):
        pass  # Нереализованный метод для вычисления площади

    def info(self):
        pass  # Нереализованный метод для вывода информации о фигуре


# Класс Square, наследующий Figure
class Square(Figure):
    def __init__(self, side_length):
        # Приватный атрибут для стороны квадрата
        self.__side_length = side_length

    def calculate_area(self):
        # Площадь квадрата: сторона * сторона
        return self.__side_length ** 2

    def info(self):
        # Возвращаем строку с информацией о квадрате
        return f"Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}^2."

    # Геттер для получения приватного атрибута
    def get_side_length(self):
        return self.__side_length

    # Сеттер для изменения значения приватного атрибута
    def set_side_length(self, side_length):
        self.__side_length = side_length


# Класс Rectangle, наследующий Figure
class Rectangle(Figure):
    def __init__(self, length, width):
        # Приватные атрибуты для длины и ширины прямоугольника
        self.__length = length
        self.__width = width

    def calculate_area(self):
        # Площадь прямоугольника: длина * ширина
        return self.__length * self.__width

    def info(self):
        # Возвращаем строку с информацией о прямоугольнике
        return f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}."

    # Геттеры для получения значений приватных атрибутов
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    # Сеттеры для изменения значений приватных атрибутов
    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width


# Запускаемая область модуля (создаем объекты и список)
if __name__ == "__main__":
    # Создаем 2 разных квадрата
    square1 = Square(4)
    square2 = Square(6)

    # Создаем 3 разных прямоугольника
    rectangle1 = Rectangle(5, 8)
    rectangle2 = Rectangle(10, 3)
    rectangle3 = Rectangle(7, 7)

    # Список, содержащий 2 квадрата и 3 прямоугольника
    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    # Цикл, вызывающий метод info для каждого объекта
    for figure in figures:
        print(figure.info())