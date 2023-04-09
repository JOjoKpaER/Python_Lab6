import math


def distance(c1, c2):
    return math.sqrt((c1[1]-c1[1])**2 - (c2[1] - c2[0])**2)


class Weapon:

    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
            return
        if (distance(actor.get_coords(),
                     target.get_coords()) > self.range):
            print("Враг слишком далеко для оружия {}".format(self.name))
            return
        print("Врагу нанесе урон оружием {} в размере {}".format(self.name, self.damage))
        target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return [self.pos_x, self.pos_y]


class BaseEnemy(BaseCharacter):

    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return "Враг на позиции ({}, {}) с оружием {}".format(self.pos_x, self.pos_y, str(self.weapon))


class MainHero(BaseCharacter):

    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []
        self.slot = 0

    def hit(self, target):
        if len(self.inventory) < 1:
            print("Я Безоружен")
            return
        if not isinstance(target, BaseEnemy):
            print("Могу ударить только врага")
            return
        self.inventory[self.slot].hit(self, target)

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
            return
        self.inventory.append(weapon)
        print("Подобрал {}".format(str(weapon)))

    def next_weapon(self):
        if len(self.inventory) <= 0:
            print("Я Безоружен")
            return
        if len(self.inventory) == 1:
            print("У меня только одно оружие")
            return
        self.slot = (self.slot + 1) % len(self.inventory)
        print("Сменил оружие на {}".format(str(self.inventory[self.slot])))

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print("Полечился, теперь здоровья {}".format(self.hp))


weapon1 = Weapon("КМ", 5, 1)
weapon2 = Weapon("ДM", 7, 2)
weapon3 = Weapon("Л", 3, 10)
weapon4 = Weapon("ЛОП", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_sellsword = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_sellsword)
armored_sellsword.move(10, 10)
print(armored_sellsword.get_coords())
main_hero = MainHero(0, 0, "КОРОЛЬ", 200)
main_hero.hit(armored_sellsword)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_sellsword)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_sellsword)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_sellsword)
main_hero.hit(armored_sellsword)
