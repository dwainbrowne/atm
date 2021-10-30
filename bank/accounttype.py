
def account(letter, my_acc):
    if letter == 'e':
        if my_acc =='1':
            print("Savings Account")
        elif my_acc == '2':
            print("Checking account")
    
    elif letter == 's':
        print ("In Spanihs")
        if my_acc == '1':	
            print ("cuenta de ahorros")#savings account
        elif my_acc == '2':
            print ("cuenta de cheques")#checking account
    else:
        print ("Invalid Selection")
    
