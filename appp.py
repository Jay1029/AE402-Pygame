class Human():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    
    def bmi(self):
        return self.weight//((self.height/100)**2)

a = Human('JAY',55,166)
print("name",a.name)
print("weight",a.weight)
print("height",a.height)
print("bmi",a.bmi())

