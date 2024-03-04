class Product:
    # data, state
    price: float
    name: str
    is_active: bool

    # behavior
    def set_price(self, price):
        # data validation
        if price < 0:
            set.price = 0
        self.price = price

    def get_price(self):
        return self.price

# constructor
    def __init__(self, name, price, is_active):
        self.price = price
        self.name = name
        self.is_active = is_active


# Parent class
class Animal:
    weight: int
    name: int

    def speak(self):
        return "Strange noise"


# child class extends Animal
class Dog(Animal):
    breed: str

    @staticmethod
    def play():
        print("Playing")

    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"
