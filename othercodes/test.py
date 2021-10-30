#Write a code that looks similar to that of an ATM:
#def Bank_code():
print ("Welcome to the Bank's Automated Teller Marketer")
language =input ("Please select your language of choice. Press e for English or s for Spanish: ")
starting_balance =1000000
account = ''
if language == 'e':
    pin = input ("Please enter your pin number")
    account = input ("Please select the account you want to access: 1 for Savings or 2 for Checking.")
if account =='1':
    amount = int(input("Enter the amount you want to withdraw: "))
    x= starting_balance - amount
    print ("With the amount you withdrew you are left with: ", x)
elif account == '2':
    amount = int(input("Enter the amount you want to deposit: "))
    x = starting_balance + amount
    print ("With the amount you deposited you are left with: ", x)

if language == 's':
    pin = input ("Ingrese su número de PIN")
    account = input ("Seleccione la cuenta a la que desea acceder: 1 para ahorros o 2 para cuentas corrientes.")
if account == '1':	
    amount = int(input("Ingrese la cantidad que desea retirar:"))
    x = starting_balance - amount
    print ("Con la cantidad que retiró, le queda:", x)
elif account == '2':
    amount = int(input("Ingrese la cantidad que desea depositar: "))
    x = starting_balance + amount
    print ("Con la cantidad que depositaste te queda: ", x)
else:
    print ("Invalid Selection")
    
choice = input("Would you like to continue? Press y for Yes or n for No.")
if choice == "y":
	language =input ("Please select your language of choice. Press e for English or s for Spanish: ")
starting_balance =1000000
account = ''
    if language == 'e':
        pin = input ("Please enter your pin number")
        account = input ("Please select the account you want to access: 1 for Savings or 2 for Checking.")
        if account =='1':
            amount = int(input("Enter the amount you want to withdraw: "))
            x= starting_balance - amount
            print ("With the amount you withdrew you are left with: ", x)
        elif account == '2':
            amount = int(input("Enter the amount you want to deposit: "))
            x = starting_balance + amount
            print ("With the amount you deposited you are left with: ", x)

    if language == 's':
        pin = input ("Ingrese su número de PIN")
        account = input ("Seleccione la cuenta a la que desea acceder: 1 para ahorros o 2 para cuentas corrientes.")
        if account == '1':	
            amount = int(input("Ingrese la cantidad que desea retirar:"))
            x = starting_balance - amount
            print ("Con la cantidad que retiró, le queda:", x)
        elif account == '2':
            amount = int(input("Ingrese la cantidad que desea depositar: "))
            x = starting_balance + amount
            print ("Con la cantidad que depositaste te queda: ", x)
        else:
            print ("Invalid Selection")
elif choice == 'n':
	print ("Have a nice day!!!")
else: 
	print ("Invalid Selction.")