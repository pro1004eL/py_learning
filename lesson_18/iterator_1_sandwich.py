
class SimpleSandwichIterator:

    def __init__(self, items):

        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

myList = ['bread', 'butter', 'cheese', 'jam']
iterator = SimpleSandwichIterator(myList)

for i in iterator:
    print(i)



