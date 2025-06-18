# SIMPLE CALCULATOR WITH TWO NUMBERS
import logging, os

use_calculator = True
num1, num2, res, op, cont_or_new = '', '', '', '', 'n'

def ask_first_num():
    try:
        return float(input("What's the first number?: "))
    except ValueError:
        logging.warning("First number must be a number.")
        return 0.0

def ask_next_num():
    try:
        return float(input("What's the next number?: "))
    except ValueError:
        logging.warning("Next number must be a number.")
        return 0.0

def ask_operation():
    try:
        user_input = input("+\n-\n*\n/\nPick an operation: ")
        assert user_input == "+" or user_input == "-" or user_input == "*" or user_input == "/"
    except AssertionError:
        logging.warning("Operation must be +, -, * or /.")
        return '?'
    return user_input

def warn_num():
    logging.warning("Next number must be a number.")

def warn_zero():
    logging.warning("Next number cannot be zero (0).")

def calculate():
    if op == '+':
        try:
            return num1 + num2
        except ValueError: warn_num()
    if op == '-':
        try:
            return num1 - num2
        except ValueError: warn_num()
    if op == '*':
        try:
            return num1 * num2
        except ValueError: warn_num()
    if op == '/':
        try:
            return num1 / num2
        except ZeroDivisionError: warn_zero()
    return 'NaN'

def show_result():
    print(f"{num1} {op} {num2} = {res}\n")

def ask_cont_or_new():
    try:
        user_input = input(f"Type 'y' to continue calculating with {res}, \
or type 'n' to start a new calculation: ")
        assert user_input == "y" or user_input == "n"
    except AssertionError:
        logging.warning("Input must be either 'y' or 'n'.")
    return user_input

while use_calculator and (cont_or_new == 'y' or cont_or_new == 'n'):
    if cont_or_new == 'y':
        num1 = res
    if cont_or_new == 'n':
        # clear terminal screen
        os.system('cls')
        num1 = ask_first_num()
    op = ask_operation()
    num2 = ask_next_num()
    res = calculate()
    show_result()
    cont_or_new = ask_cont_or_new()
