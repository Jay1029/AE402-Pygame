class Animal():
    def __init__(self,color, types, HP):
        self.color = color
        self.types = types
        self.HP = HP
    def hunt(self, time):
        self.HP = self.HP - time*5
        return self.HP
    
    def eat(self, time):
        self.HP = self.HP + time*10
        return self.HP

    def hit(self, time):
        self.HP = self.HP - time*5
        return self.hit

    def drink(self, time):
        self.HP = self.HP + time*10
        return self.drink
class Dog(Animal):
    def __init__(self,color, types, HP):
        super().__init__(color, types, HP)
    
    def barking(self):
        print('汪汪汪')
class BullDog(Dog):
    def __init__(self,color, types, HP):
            super().__init__(color, types, HP)
    
    def barking(self):
            print('吼吼吼')

Tiger = Animal('Yellow and Black','Cat',12000)
print('Tiger color:',Tiger.color)
print('Tiger types:',Tiger.types)
print('Tiger HP:',Tiger.HP)
print('Tiger hit:',Tiger.hit)
print('Tiger drink:',Tiger.drink)
#hunt:10min
print('After Hunt Tiger Hp',Tiger.hunt(10))
print('After Eat Tiger Hp',Tiger.eat(20))
print('After Tiger hit Hp',Tiger.hit(5))
john = Animal('yellow','bulldog',12000)    
peter = Dog('yellow','bulldog',12000)
chris = BullDog('yellow','bulldog',12000)