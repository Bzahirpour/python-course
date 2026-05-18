class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal): #will inherit the mammal method
    def bark(self):
        print('bark')


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
