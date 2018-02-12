class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
        print "I Am Dragon"

    def fly(self):
        self.health -= 10
        return self







dog = Dog("Luca", 0)
dragon = Dragon("Smaug", 0)

dog.walk().walk().pet().run().run().pet().display_health()
dragon.fly().fly().display_health()