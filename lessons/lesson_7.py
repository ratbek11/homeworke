import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('user.db')
cursor = connect.cursor()

# Создание таблицы users, если её нет
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(40) NOT NULL,
        age INT NOT NULL,
        hobby TEXT
    )
""")

# Создание таблицы grades, если её нет
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        grade INTEGER NOT NULL
    )
""")

connect.commit()


# Функции для работы с users
def add_user(name, age, hobby):
    """Добавляет нового пользователя"""
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"User {name} added.")


def get_all_users():
    """Выводит всех пользователей"""
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("List of all users:")

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


def get_user_by_name(name_to_find):
    """Ищет пользователя по имени"""
    cursor.execute('SELECT * FROM users WHERE name = ?', (name_to_find,))
    users = cursor.fetchall()

    if users:
        print(f"Info about {name_to_find}:")
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print(f"User {name_to_find} not found.")


# Функции для работы с grades
def add_grade(subject, grade):
    """Добавляет новую оценку в таблицу grades"""
    cursor.execute(
        'INSERT INTO grades(subject, grade) VALUES (?, ?)',
        (subject, grade)
    )
    connect.commit()
    print(f"Added grade {grade} for subject {subject}.")


def get_all_grades():
    """Выводит все оценки"""
    cursor.execute('SELECT * FROM grades')
    grades = cursor.fetchall()

    print("List of grades:")
    for row in grades:
        print(f"ID: {row[0]}, Subject: {row[1]}, Grade: {row[2]}")


# Примеры использования
add_user("John", 33, "swimming")
add_user("David", 54, "reading")
add_user("Maks", 76, "hiking")

get_all_users()

add_grade("Math", 5)
add_grade("History", 4)
add_grade("Biology", 3)

get_all_grades()

# Закрытие соединения с базой данных
connect.close()


# HOMWORKE 7

import sqlite3

def update_grade(lesson_id, new_grade):
    with sqlite3.connect('user.db') as connect:
        cursor = connect.cursor()
        cursor.execute(
            "UPDATE grades SET grade = ? WHERE id = ?",
            (new_grade, lesson_id)
        )
        connect.commit()
        print(f"Subject ID {lesson_id} updated!")

# Пример вызова
update_grade(2, 3)  # Обновит оценку для ID 2 на 3


