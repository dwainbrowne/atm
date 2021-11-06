
from comms import language
from bank import pinnumber
from bank import accounttype
from atm import receipt
from atm import transaction
from bank import savings
from bank import checking
#import languageconstants
def main_program ():
    #import accountactivity
    remainingbalancesaving = 0
    remainingbalancechecking = 0
    print ("Welcome to the Bank's Automated Teller Marketer")
    #languageconstants.constants()
    
    #Dwain Testing...

    letter = input("Please choose your language option- e for English and s for Spanish: ")
    #while letter != "e" or letter != "s":
        #letter = input("Please choose your language option- e for English and s for Spanish: ")
    #ask the user for langauge choice
    language.languagechoice(letter)

    #ask the user for their pin number
    #bank.validatepin(letter)
    pinnumber.pin(letter)

    #ask for account type
    my_acc = input ("Please select the account you want to access- 1 for Savings or 2 for Checking: ")
    #while my_acc != 1 or my_acc != 2:
        #my_acc = input ("Please select the account you want to access- 1 for Savings or 2 for Checking: ")
    accounttype.account(letter, my_acc)

    #ask for deduction or adding to the account
    remainingbalancesaving = savings.save(my_acc, letter)
    remainingbalancechecking =checking.check(my_acc, letter)
    #accountactivity.activity(letter, remainingbalancesaving, remainingbalancechecking)

    #print out based on pervious statement
    receipt.balance(my_acc, letter, remainingbalancesaving, remainingbalancechecking)
    
    selected_choice = transaction.restarttransaction()

    return selected_choice
    
