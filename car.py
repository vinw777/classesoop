class Car:
    # constructor - special method to initialize atributes
    def __init__(self, make, model, year=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price= price

    # methods
    def drive(self):
        print('Car', self.make, 'is driving')

    def info(self):
        print('Car make=', self.make, 'model=', self.model, 'year=', self.year, 'price=', self.price)
