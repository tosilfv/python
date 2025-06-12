from random import randint, shuffle

##########################################################################################################################################################################
# constant declaration
LETTERS_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SYMBOLS_LIST = ['!', '"', '#', '%', '&', '/', '(', ')', '=', '?', '^', '*', '@', '£', '$', '{', '[', ']', '}', '+', '<', '>', '|', ',', '.', '-', ';', ':', '_', '§', '½']
NUMBERS_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# variable declaration
selected_letters, selected_symbols, selected_numbers, password_str = '', '', '', ''
##########################################################################################################################################################################

# prompt user to choose the amount of different password items
num_letters = int(input('''Welcome to the PyPassword Generator!
How many letters would you like in your password?\n'''))
num_symbols = int(input('''How many symbols would you like?\n'''))
num_numbers = int(input('''How many numbers would you like?\n'''))

# add chosen amount of random list items to their corresponding strings
for letter in range(0, num_letters):
    selected_letters += LETTERS_LIST[randint(0, len(LETTERS_LIST) -1)]
for symbol in range(0, num_symbols):
    selected_symbols += SYMBOLS_LIST[randint(0, len(SYMBOLS_LIST) -1)]
for number in range(0, num_numbers):
    selected_numbers += NUMBERS_LIST[randint(0, len(NUMBERS_LIST) -1)]

# combine random items strings to one password string
password_str += selected_letters
password_str += selected_symbols
password_str += selected_numbers

# convert password string to list for shuffle to operate on
password_list = list(password_str)
print(password_list)

# shuffle changes and saves over original list and does not return a new list
shuffle(password_list)
print(password_list)

# convert password list back to string again
new_password = ''.join(password_list)

# print user the new password
print(f"Your password is: {new_password}")
