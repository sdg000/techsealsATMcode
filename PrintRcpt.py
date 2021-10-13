import random

def rcptPrint(withdrawn):
    # CHECK IF USER WOULD LIKE TO PRINT A RECEIPT FOR THE TRANSACTION
    while True:
        optn = input("Do you want a receipt for your transaction? (Y/N):  ").upper()
        
        # CHECK IF THE USER SAYS YES AND PRINT A RECEIPT FOR THE TRANSACTION i.e DISPLAY SPECIFICS OF THE TRANSACTION
        if optn == "Y":
            print(("\n \n.........Transaction Receipt............\n").upper())
            print("******************************************\n \n")
            print(("Transaction is now complete.\n").upper())                       
            print("Transaction number: "+str(random.randint(100000000000,999999999999))+"\n")
            print("Account Name: "+str(session['username']).upper()+"\n") 
            print("Amount Withdrawn: "+str(withdrawn[0])+" "+str(withdrawn[1])+"\n")      
            print("Available Balance: "+str(withdrawn[2])+"\n \n")                 
            print("*******************************************\n \n")
            print("Thank you for choosing Tech Seals Bank\n \n")
            print("*******************************************\n \n")
            break
        
        # CHECK IF THE USER SAYS NO STOP THE LOOP
        elif optn == "N":
            break   

        # CHECK IF THE USER INPUT IS INCORRECT AND ASK FOR THE CORRECT INPUT
        else:
            print("Wrong command!  Enter 'Y' for Yes and 'N' for No.\n")
            continue
    return
