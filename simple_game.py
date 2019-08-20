class Person:
    healthPoint = 100

    def attack(self):
      monster = Monster()
      monsterHealthPoint = monster.healthPoint - 10

        if monsterHealthPoint <= 0:
            print('the Monster is Dead')
        else:
            print('%d' %(monsterHealthPoint))




class Monster:
    healthPoint = 100
    def attack(self):
        personHealthPont = Person().personHealthPoint - 10

        if personHealthPont <= 0:
            print('the Person is Dead')
        else:
            print('%d' %(personHealthPont))

person = Person()


person.attack()
person.attack()
Person().attack()
person.attack()




class Car:
    carSize = 100
car = Car()
car.carSize -= 10

car.carSize