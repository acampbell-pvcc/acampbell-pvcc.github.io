# Name: Alexus Campbell
# Prog Purpose: Create a reciept for a pizza purchase

import datetime

## define global variables ##
# define tax rate and prices
SALES_TAX_RATE = .055
S_PIZZA = 9.99
M_PIZZA = 12.99
L_PIZZA = 14.99
X_PIZZA = 17.99

# define global variables
num_pizza = 0
pizza_size = 0
subtotal = 0
sales_tax = 0
total = 0

#define program functions#
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Would you like to order another pizza? (Y/N) :")
        if yesno == "n" or yesno == "N":
                another_order = False

def get_user_data():
    global pizza_size, num_pizza
    print("Palmera Pizza Sizes:")
    print("\t S for Small")
    print("\t M for Medium")
    print("\t L for Large")
    print("\t X for Extra Large")

    pizza_size = input("\nPizza Size: ")
    num_pizza = int(input("Number of pizzas: "))

def perform_calculations():
    global subtotal, sales_tax, total, pizza_size, num_pizza
    if pizza_size.upper() == "S":
        subtotal = num_pizza * S_PIZZA
    if pizza_size.upper() == "M":
        subtotal = num_pizza *  M_PIZZA
    if pizza_size.upper() == "L":
        subtotal = num_pizza * L_PIZZA
    if pizza_size.upper() == "X":
        subtotal = num_pizza * X_PIZZA
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('--------------------------------')
    print('******** PALMERA PIZZA *********')
    print('Best Homemade Pizzas in the City')
    print('--------------------------------')
    print('Pizza        $'+format (subtotal,'10,.2f'))
    print('Sales Tax    $'+format (sales_tax, '10,.2f'))
    print('Total        $'+format (total, '10,.2f'))
    print('--------------------------------')
    print(str(datetime.datetime.now()))

    #call on main program to execute#
main()
                                   
                              
