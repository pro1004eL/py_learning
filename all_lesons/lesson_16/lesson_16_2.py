
class Animal:

    def __init__(self, name):
        self.name = name
    def walk(self):
        print('walking...')

    def make_sound(self):
        print('animal sound')

class Lion(Animal):

    def __init__(self, name):
        super().__init__(name) # == Lion.__init(self, name)
        self.name = name
        self.legs = 4

    def make_sound(self):
        super().make_sound()
        print('byL ion version')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name) # 99% випадків так використовують
        self.name = name
        self.wings = 2

class Pterosawr(Lion, Bird):
    def __init__(self, name):
        self.name = name
        Lion.__init__(self, name)
        Bird.__init__(self, name)

    def make_sound(self):
        super(Lion, self).make_sound() # дуже рідко
        print('by Griffon version')

grifon = Pterosawr('Griffon')

print(grifon.name)
print(grifon.wings)
print(grifon.legs)

grifon.make_sound()





