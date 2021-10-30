def balance(my_acc, letter, saving, checking):
    if my_acc == "1":
        if letter == "e":
            print ("With the amount you withdrew you are left with: " + str(saving))
    #based on language
        elif my_acc == "2":
            print ("With the amount you deposited you are left with: " + str(checking))

    elif letter == "s":
        if my_acc == "1":
            print ("Con la cantidad que retiró, le queda:" + str(saving))
        elif my_acc == "2":
            print ("Con la cantidad que depositaste te queda: " + str(checking))
