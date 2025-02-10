class Person:
    def __init__(self, full_name: str, age: int, is_married: bool):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"Имя: {self.full_name}, Возраст: {self.age}, Женат/Замужем: {self.is_married}"


class Student(Person):
    def __init__(self, full_name: str, age: int, is_married: bool, marks: dict):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0

    def introduce_myself(self):
        subjects = ', '.join(f"{subj}: {mark}" for subj, mark in self.marks.items())
        return f"{super().introduce_myself()}, Оценки: {subjects}, Средний балл: {self.calculate_average_mark()}"


class Teacher(Person):
    base_salary = 30000  # Базовая зарплата

    def __init__(self, full_name: str, age: int, is_married: bool, experience: int):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(self.experience - 3, 0)
        return self.base_salary + (self.base_salary * 0.05 * bonus_years)

    def introduce_myself(self):
        return f"{super().introduce_myself()}, Опыт: {self.experience} лет, Зарплата: {self.calculate_salary()}"


def create_students():
    students = [
        Student("Алибек Беков", 16, False, {"Математика": 90, "Физика": 85, "Информатика": 95}),
        Student("Айгуль Кайратова", 17, False, {"Математика": 80, "Физика": 75, "Информатика": 88}),
        Student("Бектур Жолдошев", 15, False, {"Математика": 85, "Физика": 80, "Информатика": 90})
    ]
    return students


# Создание и вывод информации об учителе
teacher = Teacher("Канат Садыков", 45, True, 10)
print(teacher.introduce_myself())

# Создание и вывод информации об учениках
students = create_students()
for student in students:
    print(student.introduce_myself())
