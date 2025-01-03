class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name}'s sound {self.sound}"
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Cow(Animal):
    def __init__(self, name, age, sound, milk_volume):
        super().__init__(name, age, sound)
        self.milk_volume = milk_volume
    
    def make_milk(self):
        return f"{self.name} makes {self.milk_volume} liters of milk every day"

class Sheep(Animal):
    def __init__(self, name, age, sound, wool_volume):
        super().__init__(name, age, sound)
        self.wool_volume = wool_volume
    
    def shear(self):
        return f"{self.name} was sheared and got {self.wool_volume} kilograms wool"

class Chicken(Animal):
    def __init__(self, name, age, sound, eggs_laid):
        super().__init__(name, age, sound)
        self.eggs_laid = eggs_laid

    def lay_eggs(self):
        return f"{self.name} laid {self.eggs_laid} eggs every day"

cow = Cow("Bessie", 4, "mooo", 15)
sheep = Sheep("Woolly", 3, "baaa", 7)
chicken = Chicken("Clucky", 2, "cluck", 3)

animals = [cow, sheep, chicken]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print(animal.sleep())

print(cow.make_milk())
print(sheep.shear())
print(chicken.lay_eggs())
