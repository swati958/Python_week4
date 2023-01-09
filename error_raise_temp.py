# raise errrs example

class Animal:
    def _init_(self,name):
        self.name = name

    def sound(self):
        return NotImplementedError('you have to define this method in subclasses')

class Dog(Animal):
    def __init__(self,name,breed):
        super()._init_(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name, breed):
        super()._init_(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'

doggy = Dog('bonny', 'pug')
