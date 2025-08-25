class Coffee:

    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 3
    
class SugarDecorator:
    def __init__(self, coffee) -> None:
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2
    

coffee  = Coffee()

coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.cost())

coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_sugar.cost())
    


