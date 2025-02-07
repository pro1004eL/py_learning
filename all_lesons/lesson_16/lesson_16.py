class Wagon:
    max_pase = 10

    def __init__(self, number: int=None, is_locomotive: bool=False):

        if number is None and not is_locomotive:
            raise AssertionError('You have not put a wagon number')

        if is_locomotive:
            number = 0

        self.number = number
        self.is_locomotive = is_locomotive
        self.list_of_pass = []

    def add_pass(self, new_pass):
        if self.is_locomotive:
            return

        if len(self.list_of_pass) < 10:
            self.list_of_pass.append(new_pass)

    def __len__(self):
        return len(self.list_of_pass)

    def __str__(self):
        return f'wagon #{self.number}'

class Train:
    def __init__(self):
        self.locomotive = Wagon(number=1, is_locomotive=True)
        self.wagons = []

    def add_wagon(self, number: int = None):
        if number is None:
            number = len(self.wagons)

        while number in [k.number for k in self.wagons]:
            number += 1
        wagon = Wagon(number=number)
        self.wagons.append(wagon)


    def __add__(self, wagon: Wagon):
        return self.wagons.append(wagon)

    def __str__(self):
        return f'Train with {", ".join([str(k) for k in self.wagons])}'




if __name__ == '__main__':
    train = Train()

    print( 'Train, main locomotive: ', train.locomotive.is_locomotive)

    train.add_wagon(number=2)
    train.add_wagon()
    train.add_wagon(number=16)
    train.add_wagon(number=3)
    train.add_wagon()
    train.add_wagon(number=3)

    print(f'Train description: ', train)

    wg = Wagon(10)
    wg.add_pass({'id':1, 'name': "anton"})
    print('Train description 1:', train)
    train + wg # == train.__add__(wg)
    print('Train description 1:', train)
    print(train.wagons[-1].list_of_pass)
