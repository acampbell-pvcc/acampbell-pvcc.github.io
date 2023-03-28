# Name: Alexus Campbell
# Prog Purpose: This program finds the coat of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and prcies
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main():
    another_customer= True
    while another_customer:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("Do you have another customer? (Y/N) : ")
        if yesno =="n" or yesno == "N":
                another_customer= False

def get_user_data():
    global num_tickets
    num_tickets = int(input("How many movie tickets do you want: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-------------------')
    print('Tickets      $' + format(subtotal,'8,.2f'))
    print('Sales Tax    $' + format(sales_tax,'8,.2f'))
    print('Total        $' + format(total,'8,.2f'))
    print('-------------------')
    print(str(datetime.datetime.now()))

    ########## call on main program to execute ##########
main()
