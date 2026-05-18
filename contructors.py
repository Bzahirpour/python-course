class Point: #classes use PascalNamingConvneion
    # this is a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #defining methods in the body of the class
    def move(self):
        print('move')

    def draw(self):
        print ('draw')


point = Point(10, 20)
point.x
print(point.x)




class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi I am {self.name}')


person = Person('James')
print(person.name)
person.talk()


class BankAccount:
    def __init__(self, owner, balance): # defining the min info needed to create)
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.owner} now has ${self.balance}')

account1 = BankAccount('James', 1000)
account2 = BankAccount('Sarah', 500)

account1.deposit(200)
account2.deposit(100)



class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f'{self.name} has {self.health} left')
              
hero = Character('Arthur', 200)
enemy = Character('Orc', 1000)

hero.take_damage(10)
