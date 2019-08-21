class Person:
    healthPoint = 100

    def attack(self, monster):
        print("before attack %d" % monster.healthPoint)
        monster.healthPoint -= 10

        if monster.healthPoint <= 0:
            print('monster is dead')
        else:
            print('%d' %(monster.healthPoint))


class Monster:
    healthPoint = 100

    def attack(self, person):
        print('before attack %d' %(person.healthPoint))
        person.healthPoint -= 10

        if person.healthPoint <= 0:
            print('the Person is Dead')
        else:
            print('%d' %(person.healthPoint))



class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        point = self.ability_power*0.65 + 400
        print("티버: 피해량 %f" %(point))


annie = Annie(100,100,50)
annie.tibbers()


person = Person()
monster = Monster()
person.attack(monster)
monster.attack(person)