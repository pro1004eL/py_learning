class Auto:
    def __init__(self, model, color, engine, fuel_to_km=0.2): # magic method, конструктор

        self.model = model
        self.color = color
        self.engine = engine

        self.tank = 0

        self.__fuel_to_km = fuel_to_km

    def drive_to_town(self, distance_km):
        if self.tank / self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km * self.__fuel_to_km
            print('Driving...')

        else:
            print(f'Cant go there, have fuel only on {self.tank / self.__fuel_to_km} km.')


class Nissan(Auto):

    brand = 'NISSAN' # якщо немає self - то це class attribute
    base_country = 'Japan' # class attribute

    @classmethod
    def say_greetings(cls):
        print(f'Hello from {cls.brand}, {cls.base_country}')

    @classmethod
    def get_base_country(cls):
        return f'Created: {cls.base_country}'

    # ця ж функція для self not_class_method
    def say_greetings_not_class_method(self):
        print(f'Hello from {self.brand}, {self.base_country}')


navara = Nissan('Navara', 'Black', 5.2)
almera = Nissan('Almera', 'Grey', 1.5, fuel_to_km=0.1)


almera.say_greetings() # інстанс (функція) в класі

#Nissan.say_greetings_not_class_method() # не працює
Nissan.say_greetings_not_class_method(almera) # == almera.say_greetings_not_class_method()
almera.say_greetings_not_class_method()

print(Nissan.get_base_country())



# print(navara.brand)
#
# navara.__class__.brand = 'New NISSAN'
#
# print(navara.brand)
#
# print(navara.base_country)
#
# Nissan.base_country = 'UA'
#
# print(navara.base_country)


# navara.tank = 50
# navara.drive_to_town(400)
# navara.drive_to_town(400)

