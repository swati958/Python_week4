#special magic methods/dunder methods
# operator overloading
# polymorphism (any one thing has two or more forms)

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"
        
    # str, repr
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price}'
        # str for user and repr is for 
    def _len_(self):
        return len(self.phone_name())

    #def _mul_(self, other):
    #    return self.price * other.price

class SmartPhone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    def _len_(self):
        return len(self.phone_name())




my_phone1 = Phone('nokia', '1100', 1000)
my_phone2 = Phone('nokia' ,'1600', 1200)
my_smartphone = SmartPhone('pneplus', '5t', 33000, '16mp')
print(my_smartphone.phone_name())
print(my_phone.phone_name())

