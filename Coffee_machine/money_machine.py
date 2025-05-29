class MoneyMachine:
    CURRENCY = "€"

    VALUES = {
        "2 euros": 2.00,
        "1 euro": 1.00,
        "50 cents": 0.50,
        "20 cents": 0.20,
        "10 cents": 0.10,
        "5 cents": 0.05,
        "1 cent": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.profit} {self.CURRENCY}")
    
    def process_coins(self, cost):
        print(f"Insert Coins: {cost:.2f} €")
        for coin in self.VALUES:
            coins = input(f"How many {coin}?: ")
            try:
                int(coins)
            except ValueError:
                self.money_received += 0
                continue
            received = int(coins) * self.VALUES[coin]
            self.money_received += received
        return self.money_received
    
    def make_payment(self, cost):
        self.process_coins(cost)
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your change: {change} {self.CURRENCY}.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("There is not enough money.")
            self.money_received = 0
            return False
