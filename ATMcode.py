# DUMMY PLACEHOLDER TO TEST FUNCTION
loginDetails = [
    {
    'username':'bagna',
    'pin':1234,
    'balance':{'GHS':200, 'USD':300}
    },
    {
    'username':'angela',
    'pin':3333,
    'balance':{'GHS':600, 'USD':150}
    }
]


# WITHDRAWAL AND BALANCE UPDATE FUNCTION
def withdrawUpdate():
    print ('########################################### ATM WITHDRAWAL #####################################################\n \n')
    print (('Tech Seals Banking App\n \n Please follow the instructions for a successful transaction').upper())

    def withdrawRequest():
       # TAKE CURRENCY INPUT 
        while True:
            print (' \n******************************************* CURRENCY *****************************************************\n \n')
            currency = str(input('Withdraw from USD or GHS account (Type D for USD / G for GHS):\n').upper())

            # CHECK IF THE VALUE INPUTTED IS CORRRECT
            # IF THE VALUE IS NOT CORRECT DO THIS
            if currency not in ('D', 'G'):
                print (' \n_______________________________________________________________________________\n  \n')
                print("Invalid choice. Please try again")
                print (' \n_______________________________________________________________________________\n  \n')
                continue
            
            # IF THE VALUE IS CORRECT MOVE TO THE NEXT STEP
            elif currency == 'D':
                currency = 'USD'
                break
            elif currency == 'G':
                currency = 'GHS'
                break
        
        # TAKE AMOUNT INPUT
        while True:
            print (' \n******************************************* AMOUNT *********************************************************\n \n')

            # CHECK THE AMOUNT VALUE 
            try:
                amount = int(input('Please enter the amount you want to withdraw:\n'))

                # IF THE WITHDRAWAL AMOUNT IS MORE THAN THE USERS BALANCE DO THIS
                if amount >= loginDetails[0]['balance'][currency]:
                    print (' \n_______________________________________________________________________________\n  \n')
                    print ('Insufficient Funds. Try Again: \n')
                    print (' \n_______________________________________________________________________________\n  \n')
                    continue

                # IF THE WITHDRAWAL AMOUNT IS LESS THAN THE USERS BALANCE MOVE TO THE NEXT STEP
                elif amount < loginDetails[0]['balance'][currency]:
                    minimumBalance = 50
                    balanceAfterWithdraw = loginDetails[0]['balance'][currency] - amount
                    
                    # Check if balance after withdrawal is less than minimumBalance
                    if balanceAfterWithdraw < minimumBalance:
                        print (' \n_______________________________________________________________________________\n  \n')
                        print ('Insufficient remaining balance after withdrawal.\n You must have a minimum balance of '+currency+' 50. Try Again: \n')
                        print (' \n_______________________________________________________________________________\n  \n')
                        continue
                    else:
                        break

            # IF THE USER DOES NOT INPUT WHOLE NUMBERS DO THIS
            except ValueError:
                print (' \n_______________________________________________________________________________\n  \n')
                print ('Invalid input. Please enter a number')
                print (' \n_______________________________________________________________________________\n  \n')
                continue
        
        return currency,amount
            
    
    # RUN THE WITHDRAWAL REQUEST FUNCTION
    while True: 
        withdrawalValues = withdrawRequest()
        currency = withdrawalValues[0]
        amount = withdrawalValues[1]
        
        print (' \n******************************************* CONFIRM AMOUNT WITHDRAWAL *********************************************************\n \n')
        confirmation = str(input('Please confirm withdrawal amount: ' + currency + ' '+ str(amount) + '\n Y to continue / N to try again: ').upper())
        
        if confirmation not in ('Y', 'N'):
            print (' \n_______________________________________________________________________________\n  \n')
            print ("Sorry I didn't understand that. Please start again.")
            print (' \n_______________________________________________________________________________\n  \n')
            continue
        elif confirmation == 'N':
            continue
        elif confirmation == 'Y':
            break

    print (' \n******************************************* SUCCESSFUL TRANSACTION *********************************************************\n \n')
    
    # SAVE THE WITHDRAWN AMOUNT AND CURRENCY
    amountWithdrawn = amount
    currencyWithdrawn = currency
    print (' \n_______________________________________________________________________________\n  \n')
    print ('Successful Withdrawal of '+ currencyWithdrawn +' '+ str(amountWithdrawn))

    # SUBTRACT WITHDRAWN AMOUNT FROM USERS CURRENT BALANCE AND SAVE IT TO newBalance VARIABLE
    print ('Previous Balance: '+ currencyWithdrawn +' '+ str(loginDetails[0]['balance'][currency]))
    newBalance = loginDetails[0]['balance'][currency] - amountWithdrawn
    
    # UPDATE USERS BALANCE TO THE NEW BALANCE
    loginDetails[0]['balance'][currency] = newBalance
    print ('New Balance: '+ currencyWithdrawn +' '+ str(loginDetails[0]['balance'][currency]))
    print (' \n_______________________________________________________________________________\n  \n')

# RUN THE WITHDRAW UPDATE FUNCTION
withdrawUpdate()