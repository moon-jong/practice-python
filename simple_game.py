class Person:
    healthPoint = 100

    def attack(self, monster2):
        print("before attack %d" % monster2.healthPoint)
        monster2.healthPoint -= 10
        monsterHealthPoint = monster2.healthPoint

        if monster2.healthPoint <= 0:
            print('monster is dead')
        else:
            print('%d' %(monster2.healthPoint))


class Monster:
    healthPoint = 100

    def attack(self):
        personHealthPont = Person().personHealthPoint - 10

        if personHealthPont <= 0:
            print('the Person is Dead')
        else:
            print('%d' %(personHealthPont))



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
class Car:
    carSize = 100
car = Car()
car.carSize -= 10

car.carSize

person = Person()
monster = Monster()
person.attack(monster)



def f(N):
    print(N)
    if N >0:
        f(N-1)
f(5)