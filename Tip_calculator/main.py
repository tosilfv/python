print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10%, 12%, or 15%? "))
bill_splitters = int(input("How many people to split the bill? "))
tip_amount = total_bill * (tip_percent / 100)
total = (total_bill + tip_amount) / bill_splitters
print(f"Each person should pay: ${total}")