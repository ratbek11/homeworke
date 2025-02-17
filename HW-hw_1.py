
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def introduce(self):
        print(f"Hi my name is {self.name}. My level is '{self.lvl}'. My hels power is '{self.hp}' ")

    def is_adult(self):
        return self.lvl >= 10

optimus = Hero("optimus",5000, 34)
optimus.introduce()

#extra heros
optimus2 = Hero("optimus2",7653, 4)
optimus3 = Hero("optimus3",345, 56)

print(optimus.name, "взрослый?", optimus.is_adult())
print(optimus2.name, "взрослый?", optimus2.is_adult())
print(optimus3.name, "взрослый?", optimus3.is_adult())



# Создание экземпляра и вызов introduce
hero1 = Hero("Артас", 5, 100)
hero1.introduce()

# Создание нескольких героев и проверка is_adult
hero2 = Hero("Тралл", 12, 150)
hero3 = Hero("Джайн", 8, 120)


















# class ShildeHero(Hero):
#     pass
#
# archi = ShildeHero("archi",5000, 34)
# archi.action()
#
#
#     def __init__ (self , name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Hi my name is {self.name}")
#
# ardaguler = Person("ardaguler",15)
#
# ardaguler.introduce()
