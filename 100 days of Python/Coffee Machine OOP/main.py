from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

running = Trueespre

while running:

    options = menu.get_items()

    user_choice = input(f'What drink would you like? {options}')
    

    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report() 
    elif user_choice == 'off':
        running = False
    else:
        order = menu.find_drink(user_choice)
        if order != None:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)
