# AUCTION: ADD BIDS, WIN BID
import logging, os

YES, NO = 'yes', 'no'
play_game = True
other_bidders, name, bid, winner_name, winner_bid =\
    YES, '', '', '', ''
bid_dict = {}

def show_bid_title():
    print('''
                         ___________
                                   /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_______________| |_..-'
                          |_______| '-'---------------.-.-
                          )       (
                                   \\
                        .___________.
                       /_____________\\
          ''')

def ask_name():
    try:
        user_input = input("What is your name?: ")
        assert len(user_input) > 0
    except AssertionError:
        logging.warning("Name cannot be empty.")
    return user_input

def ask_bid():
    try:
        user_input = input("What is your bid?: $")
        # check if input is a number
        assert user_input.isdigit()
    except AssertionError:
        logging.warning("Input must be a number.")
    try:
        # check if input is not a float
        assert user_input.isdecimal()
    except AssertionError:
        logging.warning("Input cannot be a decimal number.")
    # convert number to int
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        user_input = 0
    return user_input

def ask_other_bidders():
    try:
        user_input = input("Are there any other bidders? Type 'yes or 'no'.\n")
        assert user_input == "yes" or user_input == "no"
    except AssertionError:
        logging.warning("Other bidders must be either 'yes' or 'no'.")
    return user_input

def add_bid(name, bid):
    bid_dict[name] = bid

def select_winner():
    biggest_name = ''
    biggest_bid = 0
    for name, bid in bid_dict.items():
        if bid > biggest_bid:
            biggest_bid = bid
            biggest_name = name
        #if same bid amount is already made by other bidder\
        #select the first bidder as winner
        elif bid == biggest_bid:
            continue
    return biggest_name, biggest_bid

def show_winner():
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")

# show hammer
show_bid_title()

# play game
while play_game == True and other_bidders == YES:
    name = ask_name()
    bid = ask_bid()
    add_bid(name, bid)
    other_bidders = ask_other_bidders()
    if other_bidders == YES:
        # clear terminal screen
        os.system('cls')
        continue
    if other_bidders == NO:
        # destructure return values
        winner_name, winner_bid = select_winner()
        show_winner()
        break
