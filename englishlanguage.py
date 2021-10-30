import accounttype

def english():
    letter=input("Please choose your language option- e for English and s for Spanish: ")
    if letter == 'e':
        accounttype.account()
        return letter
    else:
        print("Invalid selection")
        exit