# CAESAR CIPHER
import logging
from markupsafe import escape

TOTAL_NUM_ASCII, ENCODE, DECODE, YES, NO = 255, "encode", "decode", "yes", "no"
play_game = True
run_again = YES
shift_num, shifted_val = 0, 0
enc_or_dec, message, result =\
    "", "", ""
message_list_orig, message_list_shft, orders_list_orig,\
    orders_list_shft, characters_list =\
    [], [], [], [], []

def show_caesar_title():
    print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88''')

def ask_enc_or_dec():
    try:
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        assert user_input == "encode" or user_input == "decode"
    except AssertionError:
        logging.warning("Input must be either 'encode' or 'decode'.")
    return user_input

def ask_message():
    return input("Type your message:\n")

def ask_shift_num():
    try:
        return int(input("Type the shift number:\n"))
    except ValueError:
        logging.warning("Input must be a number.")

def ask_run_again():
    return input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

def show_encoded_result():
    print(f"Here's the encoded result: {result}")

def show_decoded_result():
    print(f"Here's the decoded result: {result}")

def say_goodbye():
    print("Goodbye")

def prepare_message(msg):
    # validate msg
    if not isinstance(msg, str):
        logging.warning("Input must be a string.")
    if len(msg) == 0 or len(msg) > 50:
        logging.warning("Input must be between 1 and 50 characters.")
    # sanitize msg
    safe_message = escape(msg)
    return safe_message.strip().lower()

def check_overflow(encryption, value, shift_num):
    # if shift is multiples of TOTAL_NUM_ASCII, subtract multiples and only use the remainder
    overflow_rounds = shift_num // TOTAL_NUM_ASCII
    # if overflow rounds is negative, make it positive
    if overflow_rounds < 0: overflow_rounds *= -1
    if overflow_rounds > 0:
        shift_num = (shift_num - (overflow_rounds * TOTAL_NUM_ASCII)) % TOTAL_NUM_ASCII
    if encryption == ENCODE:
        # e.g. if shift would result in character of order 256, go to order 1
        if value + shift_num < 256:
            return value + shift_num
        else:
            return (value + shift_num) - TOTAL_NUM_ASCII
    if encryption == DECODE:
        # e.g. if shift would result in character of order 0, go to order 255
        if value - shift_num > 0:
            return value - shift_num
        else:
            return (value - shift_num) + TOTAL_NUM_ASCII

def encrypt_message(encryption, msg):
    # make msg into list
    message_list_orig = list(msg)
    # save message list character orders
    for char in message_list_orig:
        orders_list_orig.append(ord(char))
    # shift original orders list characters by shift number
    for index, value in enumerate(orders_list_orig):
        shifted_val = check_overflow(encryption, value, shift_num)
        orders_list_shft.append(shifted_val)
    # save shifted order characters to shifted orders list
    for order in orders_list_shft:
        message_list_shft.append(chr(order))
    # make list into msg
    result = "".join(message_list_shft)
    return result

# print title
if play_game:
    show_caesar_title()

# play game
while play_game and run_again == YES:
    # prompt user play choices
    enc_or_dec = ask_enc_or_dec()
    message = ask_message()
    message = prepare_message(message)
    shift_num = ask_shift_num()
    # calculate and show result
    if enc_or_dec == ENCODE:
        result = encrypt_message(ENCODE, message)
        show_encoded_result()
    if enc_or_dec == DECODE:
        result = encrypt_message(DECODE, message)
        show_decoded_result()
    # prompt user quit choices
    run_again = ask_run_again()
    if run_again == YES:
        # clear values
        shift_num, shifted_val = 0, 0
        enc_or_dec, message, result =\
            "", "", ""
        message_list_orig, message_list_shft, orders_list_orig,\
            orders_list_shft, characters_list =\
            [], [], [], [], []
        continue
    if run_again == NO:
        play_game = False
        say_goodbye()
