class Hero:
    def __init__(self, name, hp, ):
        self.name = name
        self.hp = hp

    def attack(self):
        return f"{self.name} do attack!"

    def action(self):
        return f"{self.name} move forvard"


class Archer(Hero):
    def __init__(self, name: str, hp: int, arrows: int):
        super().__init__(name, hp, )
        self.arrows = arrows

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} did attack! . Arrows sum is {self.arrows}"
        else:
            return f"{self.name} can not do attack. Cause arrows is end! "

hero = Hero("Madi", 500)
archi = Archer("Bable",400, 10)

print(hero.attack())
print(hero.action())
print(archi.action())
print(archi.attack())