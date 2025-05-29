from doctest import run_docstring_examples
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

def test_coffee_machine():
    """ --- DOCTEST ---
    Money Machine Report
    >>> money_machine.report()
    Money: 0 €

    Coffee Maker Report
    >>> coffee_maker.report()
    Water: 500 ml
    Milk: 500 ml
    Coffee: 500 g
    """

run_docstring_examples(test_coffee_machine, globals(), True)
