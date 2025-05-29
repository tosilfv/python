from menu_item import MenuItem

class Menu:
    currency = '$'

    def __init__(self):
        self.items = [
            MenuItem('espresso', cost=3.5, water=50, milk=0, coffee=18),
            MenuItem('latte', cost=2.5, water=200, milk=150, coffee=24),
            MenuItem('cappuccino', cost=1.5, water=250, milk=50, coffee=24)
        ]

    def get_items(self):
        items = ""
        for item in self.items:
            items += f"{item.name}/"
        return items

    def find_drink(self, order_name):
        for item in self.items:
            if item.name == order_name:
                return item

