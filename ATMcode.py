#!/usr/bin/env python3

import getpass
import random


#Database of user accounts
userArray=[{'username':'aba', 'pin':2121, 'balance':{'GHS':100000, 'USD':80000} },
{'username':'akosua', 'pin':4000, 'balance':{'GHS':280, 'USD':450} },
{'username':'eben', 'pin':5461, 'balance':{'GHS':800, 'USD':300} },
{'username':'bet', 'pin':3197, 'balance':{'GHS':995000, 'USD':980000} },
{'username':'david', 'pin':3216, 'balance':{'GHS':789, 'USD':250} },
{'username':'dna', 'pin':1234, 'balance':{'GHS':25000, 'USD':15000} },
{'username':'dave', 'pin':1034, 'balance':{'GHS':250, 'USD':8000} },
{'username':'esinam', 'pin':1110, 'balance':{'GHS':5000, 'USD':20000} },
{'username':'emmanuel', 'pin':2145, 'balance':{'GHS':8943, 'USD':2153} },
{'username':'van', 'pin':2111, 'balance':{'GHS':15000, 'USD':80000} },
{'username':'bagna', 'pin':7438, 'balance':{'GHS':555000, 'USD':300000} } ]


# LANDING MESSAGE
print ('########################################### TECH SEALS BANK #####################################################\n \n')
print ('Please enter your credentials to login\n \n')


# Main Interaction Menu after Successful LogIn       
def atmMenu():

    # DISPLAY WELCOME MESSAGE
    print (' \n_______________________________________________________________________________\n  \n')
    print (('Tech Seals Banking App\n \nPlease follow the instructions for a successful transaction').upper())
    print (' \n_______________________________________________________________________________\n  \n')
    print ("Welcome " + str(userName.upper()) + "\n \nWhat would you like to do today?\n \n")
    
    # CHECK USER TRANSACTION SELECTION
    while True:
        # REQUEST USER TRANSACTION SELECTION
        print ("Type the number associated with the transaction you want to perform and \nPress enter to select")
        print (' \n_______________________________________________________________________________\n  \n')   
        transaction = int(input("1) Check Balance  2) Make Withdrawal  3) Mobile Money  99) Quit / Log Out\n \n"))

        # CHECK IF USER WANTS TO CHECK BALANCE AND RUN
        if transaction == 1:
            # RUN THE BALANCE CHECK FUNCTION
            crntBalance()
            pause = input('\n \nPress Enter to return to the Main Menu ')
            continue
            
        # CHECK IF USER WANTS TO MAKE A WITHDRAWAL AND RUN
        elif transaction == 2:
            # RUN THE WITHDRAWAL FUNCTION AND SAVE ALL OUTPUTS TO THE VARIABLE
            withdrawn = withdrawUpdate()
            # RUN THE RECEIPT REQUEST FUNCTION
            rcptPrint(withdrawn)
            break
        
        # CHECK IF USER WANTS TO MAKE A MOBILE MONEY WITHDRAWAL
        #elif transaction == 3:
            # RUN THE MOBILE MONEY FUNCTION
            #withdrawn = withdrawUpdate()
           # break
        
        # CHECK IF USER WANTS QUIT OR LOG OFF
        elif transaction == 99:
            while True:
                # REQUEST INPUT FROM USER
                print (' \n_______________________________________________________________________________\n  \n')
                quitConfirm = str(input('\n \nAre you sure you want to quit? (Y/N):  ')).upper()
                print (' \n_______________________________________________________________________________\n  \n')

                # IF USER SAYS YES END PROGRAM
                if quitConfirm == 'Y':
                    print("""
                        -----------------------------------------
                        | Thank you for choosing Tech Seals Bank |
                        |         Visit us again!                |
                        -----------------------------------------
                    """)
                    exit()

                # IF USER SAYS NO RELOAD THE MAIN MENU
                elif quitConfirm == 'N':
                    break
                
                # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
                else:
                    print (' \n_______________________________________________________________________________\n  \n')
                    print ('Invalid input. Try again')
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue

            continue


    # CHECK IF USER WOULD LIKE TO PERFORM ANOTHER TRANSACTION
    while True:
        # REQUEST INPUT FROM USER
        print (' \n_______________________________________________________________________________\n  \n')
        backtoMain = str(input('Would you like to perform another another transaction? Y/N :  ')).upper()
        print (' \n_______________________________________________________________________________\n  \n')

        # IF USER SAYS YES RELOAD THE MAIN MENU
        if  backtoMain == 'Y':
            return atmMenu()
        
        # IF USER SAYS NO END PROGRAM
        elif  backtoMain == 'N':
            print("""
                -----------------------------------------
                | Thank you for choosing Tech Seals Bank |
                |         Visit us again!                |
                -----------------------------------------
            """)
            exit()

        # IF USER RESPONSE IS INVALID ASK FOR A VALID INPUT
        else:
            print ('Invalid input. Try again')
            continue


# WITHDRAWAL AND BALANCE UPDATE FUNCTION
def withdrawUpdate():
    # DISPLAY FUNCTION MESSAGE
    print ('########################################### ATM WITHDRAWAL #####################################################\n \n')
    print (('Tech Seals Banking App\n \n Please follow the instructions for a successful transaction').upper())

    # SET A MINIMUM BALANCE LIMIT
    minimumBalance = 50

    # SET A MAXIMUM WITHDRAWAL LIMIT
    maxWithdrawal = 5000

    # TAKE USER INPUTS ON WITHDRAWAL SPECIFICS
    def withdrawRequest():
       # TAKE CURRENCY INPUT 
        while True:
            print (' \n******************************************* CURRENCY *****************************************************\n \n')
            currency = str(input('Withdraw from USD or GHS account (Type D for USD / G for GHS):\n').upper())

            # IF THE USER INPUT IS INCORRECT RESTART FUNCTION
            if currency not in ('D', 'G'):
                print (' \n_______________________________________________________________________________\n  \n')
                print("Invalid choice. Please try again")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
            
            # IF THE USER INPUT IS CORRECT ASSIGN THE SELECTED CURRENCY TO THE VARIABLE CURRENCY
            elif currency == 'D':
                currency = 'USD'
                break
            elif currency == 'G':
                currency = 'GHS'
                break
        
        # TAKE AMOUNT INPUT
        while True:
            print (' \n******************************************* AMOUNT *********************************************************\n \n')

            # CHECK THE AMOUNT VALUE INPUTTED
            try:
                amount = int(input('Please enter the amount you want to withdraw:\n'))

                # IF THE WITHDRAWAL AMOUNT IS MORE THAN THE USERS BALANCE DO THIS
                if amount >= userBalance[currency]:
                    
                    # ALLOW USER TO DECIDE TO TR AGAIN OR RETURN TO MAIN MENU
                    while True:
                        stopContinue = str(input("Insufficient Funds\n \nWould you like to try again or return to the main Menu? \n Type 'Y' to try agin or Type 'N' to return to the main Menu: \n")).upper()

                        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
                        if stopContinue not in ('Y', 'N'):
                            print ('Invalid Input, try again.')
                            continue
                        
                        # IF USER SAYS YES RESTART FUNCTION AND TAKE CORRECT AMOUNT INPUT
                        elif stopContinue == 'Y':
                            break

                        # IF USER SAYS NO RETURN TO THE MAIN MENU
                        elif stopContinue == 'N':
                            return atmMenu()
                            
                    continue

                # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
                elif amount < userBalance[currency]:
                    # CHECK USER BALANCE AFTER SPECIFIED WITHDRAWAL AMOUNT IS WITHDRAWN
                    balanceAfterWithdraw = userBalance[currency] - amount
                    
                    # CHECK IF BALANCE AFTER WITHDRAWAL IS LESS THAN MINIMUM ALLOWED BALANCE AND ASK USER TO TRY AGAIN
                    if balanceAfterWithdraw < minimumBalance:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Insufficient remaining balance after withdrawal.\n You must have a minimum balance of '+ currency + ' ' +str(minimumBalance) +'. Try Again: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    # CHECK IF WITHDRAWAL AMOUNT IS GREATER THAN MAXIMUM WITHDRAWAL LIMIT AND ASK USER TO TRY AGAIN
                    elif amount > maxWithdrawal:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Sorry. You can not withdraw more than '+ currency + ' ' + str(maxWithdrawal) +'. Try Again: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue

                    else:
                        break
                

            # IF THE USER DOES NOT INPUT WHOLE NUMBERS ASK USER TO TRY AGAIN
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Invalid input. Please enter a number')
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        # HOLD CURRENCY AND AMOUNT SPECIFIED BY USER
        return currency,amount
            
    
    # RUN THE WITHDRAWAL REQUEST FUNCTION
    while True: 
        # SAVE CURRENCY AND AMOUNT SPECIFIED BY USER INTO THE VARIABLE
        withdrawalValues = withdrawRequest()
        # SAVE CURRENCY SPECIFIED BY USER INTO THE VARIABLE
        currency = withdrawalValues[0]
        # SAVE AMOUNT SPECIFIED BY USER INTO THE VARIABLE
        amount = withdrawalValues[1]
        
        # PROMPT USER TO CONFIRM WITHDRAWAL AMOUNT
        print (' \n******************************************* CONFIRM WITHDRAWAL AMOUNT *********************************************************\n \n')
        confirmation = str(input('Please confirm withdrawal amount: ' + currency + ' '+ str(amount) + '\n Y to continue / N to change amount: ').upper())
        
        # IF THE USER INPUT IS INCORRECT ASK FOR CORRECT INPUT
        if confirmation not in ('Y', 'N'):
            print (' \n_______________________________________________________________________________\n  \n')
            print ("Sorry I didn't understand that. Please start again.")
            print (' \n_______________________________________________________________________________\n  \n')
            continue

        # IF THE USER SAYS NO ALLOW USER CHANGE VALUES
        elif confirmation == 'N':
            continue

        # IF THE USER SAYS YES CONFIRM SUCCESSFUL WITHDRAWAL IN NEXT STEP
        elif confirmation == 'Y':
            break
    
    # DISPLAY SUCCESSFUL WITHDRAWAL MESSAGE
    print (' \n******************************************* SUCCESSFUL WITHDRAWAL *********************************************************\n \n')
    print ('SUCCESS!')

    # SAVE THE WITHDRAWN AMOUNT AND CURRENCY
    amountWithdrawn = amount
    currencyWithdrawn = currency

    # DISPLAY AMOUNT WITHDRAWN TO USER
    print (' \n_______________________________________________________________________________\n  \n')
    print ('Successful Withdrawal of '+ currencyWithdrawn +' '+ str(amountWithdrawn))

    # DISPLAY USERS PREVIOUS BALANCE
    print ('Previous Balance: '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    # SUBTRACT WITHDRAWN AMOUNT FROM USERS CURRENT BALANCE AND SAVE IT TO newBalance VARIABLE
    newBalance = userBalance[currency] - amountWithdrawn
    
    # UPDATE USERS BALANCE TO WITH NEW BALANCE
    userBalance[currency] = newBalance
    # DISPLAY USERS UPDATED BALANCE
    print ('New Balance: '+ currencyWithdrawn +' '+ str(userBalance[currency]))
    print (' \n_______________________________________________________________________________\n  \n')
    print ('Thank You For Banking With Us!')
    print (' \n_______________________________________________________________________________\n  \n')

    # HOLD USERS SPECIFIED CURENCY, AMOUNT AND CURRENT BALANCE AFTER WITHDRAWAL
    return currencyWithdrawn, amountWithdrawn, newBalance


# PRINT RECEIPT FUNCTION
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


# CHECK CURRENT BALANCE FUNCTION
def crntBalance():    

    while True:
        print ('########################################### BALANCE CHECK #####################################################\n \n')
        currency = str(input("What account balance would you like to check: \nType 'G' for GHS or 'D' for USD: ")).upper()
        if currency == 'G':
            currency = 'GHS'
            break                    

        elif currency == 'D':
            currency = 'USD'
            break

        else:
            print (' \n_______________________________________________________________________________\n  \n')
            print("Invalid Input. Please Type 'G' for GHS or 'D' for USD")        
            print (' \n_______________________________________________________________________________\n  \n')    
            continue


    availableBalance = userBalance[currency]
    print (' \n_______________________________________________________________________________\n  \n')
    print (('Your available '+ currency +' account balance is:\n \n').upper())
    print (currency +' '+ str(availableBalance ))
    print (' \n_______________________________________________________________________________\n  \n')
  

# USER LOGIN IDENTITY VERIFICATION FUNCTION
def userLogin(userName):

    for userdata in userArray:

        sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 

        # Checks for user existence and says a welcome message

        if userName == userdata['username']:
            found = True
            sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
            break  
            
        else:
            found = False
            pass          

    
    return sessiondata # Returns the value of sessiondata after userLogin() is run,  so we can use in the continuing code 


def updatePin():
        
    #user inputs pin
    print("A confirmation code has been sent to your phone")
    
    verificationCode = random.randint(1000,9999)

    print(verificationCode)
    
    #after the user has been verified, he/she proceeds with the change
    while True:
        
        codeVerify = int(input("Enter verification code here: "))
        
        if codeVerify == verificationCode:
            while True:
                newPin = int(getpass.getpass(" Enter new 4 digit pin: "))
                newPinConfirm = int(getpass.getpass(" Please repeat new 4 digit pin: "))
                
                if newPin == newPinConfirm:
                    print("Congratulations! Your pin has been changed!")
                    session['pin'] = newPin
                    pause = input('Press Enter to return to the main menu. ')
                    break

                elif newPin != newPinConfirm:
                    print('Sorry Pin codes do not match. Please Try again.')
                    continue
            break

        elif codeVerify != verificationCode:
            print("Wrong Verification code entered. Please enter code again")
            continue
    
    return
    

# USER LOGIN PIN VERIFICATION FUNCTION
def pinVerify(userPin):
    
    def pinChangeRequest():
        while True:
            pinChange = str(input('Forgot Pin? Reset (Y/N):  ')).upper()

            if pinChange == 'Y':
                updatePin()
                return atmMenu()

            elif pinChange == 'N':
                print("""
                    -----------------------------------------
                    | Thank you for choosing Tech Seals Bank |
                    |         Visit us again!                |
                    -----------------------------------------
                """)
                exit()

            else:
                print ('Invalid input. Try again')
                continue

    
    valid = False
    
    for attempt in range(4):
        print ("\n \nEnter your pin to Proceed\n")
            
        pin = str(getpass.getpass("Enter your pin: "))
        
        if userPin == pin :
            valid = True
            break

        else:
            print (' \n_______________________________________________________________________________\n  \n')
            print ('Incorrect Pin. Try again')
            print (' \n_______________________________________________________________________________\n  \n')
            continue
    
    if attempt == 3:
        pinChangeRequest()
    
    
            
    return atmMenu() 


# STORE USER'S USERNAME INPUT TO SPECIFIED VARIABLE
userName = str(input("Username: ")).lower()


# RETRIEVE SPECIFIED USER DETAILS FROM DICTIONARY TO SPECIFIED VARIABLE
session = userLogin(userName)


# RETRIEVE SPECIFIED USER PIN AND STORE TO VARIABLE
userPin = str(session['pin'])


# RETRIEVE SPECIFIED USER BALANCE AND STORE TO VARIABLE
userBalance = session['balance']


# RUN PIN VERIFICATION FUNCTION
pinVerify(userPin)
