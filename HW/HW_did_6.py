import sqlite3

connect = sqlite3.connect('user.db')

# HAnd with pen
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    name VARCHAR (40) NOT NULL,
    age INT NOT NULL,
    hobby TEXT
    )
""")


# Сохранение изменений
connect.commit()


def add_user(name, age, hobby):

    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f" User {name} added ")


add_user("John", 33 , "swimming")
add_user("David", 54 , "read")
add_user("Maks", 76 , "hit")
add_user("Tomas", 33 , "fly")
add_user("Ederson", 74 , "take")

def get_all_users():

    cursor.execute('SELECT *FROM users')
    users = cursor.fetchall()
    print(users)
    print("List of all users ")

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")


def get_user_by_name():
    name_to_find = "Ederson"
    cursor.execute('SELECT * FROM users WHERE name = ?', (name_to_find ,))
    users = cursor.fetchall()
    print(users)

    if users:
        print("inf about this person")
        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print("User is not found")

get_user_by_name()
get_all_users()
connect.close()

