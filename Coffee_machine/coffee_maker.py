class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 500,
            "coffee": 500
        }

    def report(self):
        print(f"""Water: {self.resources["water"]} ml\nMilk: {self.resources["milk"]} ml\nCoffee: {self.resources["coffee"]} g""")
    
    def is_resource_sufficient(self, option):
        is_sufficient = True
        for ingredient in option.ingredients:
            if option.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry, there is not enough of {ingredient}.")
                is_sufficient = False
        return is_sufficient
    
    def make_coffee(self, option):
        for ingredient in option.ingredients:
            self.resources[ingredient] -= option.ingredients[ingredient]
        print(f"Your order for ☕️ {option.name} is completed.")
