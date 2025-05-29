from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

OPTIONS = menu.get_items().split("/")
user_order = ""

while user_order != "q":
    user_order = input(f"What would you like? ({menu.get_items()}), q to quit: \n")

    if len(user_order) == 0:
        continue
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order in OPTIONS:
        option = menu.find_drink(user_order)
        can_make = coffee_maker.is_resource_sufficient(option)
        if can_make:
            payment_ok = money_machine.make_payment(option.cost)
            if payment_ok:
                coffee_maker.make_coffee(option)
