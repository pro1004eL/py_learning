
class Car:
    def __init__(self, brand, model, start_engine):
        self.brand = brand
        self.model = model
        self.start_engine = start_engine
        self.tank = 0

    def got_somewhere(self, amount_in_km): # incapsulation
        if self.tank >= amount_in_km:
            self.tank = self.tank - amount_in_km
            print('Driving...')
        else:
            print("Can\'t go - have not enough fuel")

    def set_tank(self, value):
        self.tank = value



camry = Car(brand='Toyota', model='Camry', start_engine='3.5')

camry.set_tank(50)

camry.got_somewhere(40)
camry.got_somewhere(40)




class Fruit:
    def __init__(self, color):
        self.color = color

apple = Fruit('green')
orange = Fruit(color='orange')


class Animal:

    base_class = 'Animal class asd'
    def speak(self):
        print('Animal sound')

    def go_sleep(self):
        print('I go to sleep')


class Dog(Animal):
    def speak(self):
        print('Gav!')

class Cat(Animal):
    def speak(self): # поліморфізм
        print('Mrrr!')

class Cat_chield(Cat):
    def speak(self):
        print('miay-miysqwe')


# def make_sound(animal):
#     return animal.speak()

barsik = Dog() # створення інстатнсу (екземпляру) класу Dog
margosha = Cat() # створення інстатнсу (екземпляру) класу Cat
unknown = Animal()
eva = Cat_chield()

eva.go_sleep()
barsik.speak()
margosha.speak()
margosha.go_sleep()
unknown.go_sleep()






