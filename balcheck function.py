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

def crntBalance():  #FUNCTION TO ALLOW USERS TO CHECK THEIR BALANCE.

       

                
    #username = loginDetails['username']
    #crntBalance1=loginDetails['balance'][currency]
    
    while True:
            try:
                Balance_check = str(input('Would you want to check your current balanct ? Y / N')).upper()
      
    
                                      
                if Balance_check == 'Y':
                                while True:
                                        try:
                                            currency = int(input('\n Select preffered currency: \n(1) Ghs  \n(2) Usd...  '))
                                            if currency == 1:
                                                currency = 'GHS'
                                                break                    
    
                                            elif currency == 2:
                                                currency = 'USD'
                                                break
                                            else:
                                                 print('enter 1 or 2')            
                                                 continue
                                        except ValueError:
                                              print('invalid input')
                                              continue

                                #print(username + ', your current balance is: ') 
                                print(currency + str(crntBalance1)) #crntBalance1 SHOULD NOT BE PRINTED AS STR, IT SHOULD APPEAR AS INT OR FLOAT.
                                break

                elif Balance_check == 'N':
                            while True:
                                    try:
                                        other_request = str(input('Would you like to perform another transaction?  Y / N ')).upper()
                                        if other_request == 'Y':
                                            menu()
                                            break
                                            continue

                                        elif other_request == 'N':
                                             print('thank you for banking with us')
                                             quit()
                                             
                                         

                                    #if print('Enter Y / N'):

                                     
                                         #continue
                                        else:
                                            print('enter Y/N')
                                            continue
                                        
                                    except ValueError:
                                            print('invalid input')
                                            continue

                else:
                    print('Invalid Input')

            except ValueError:
                    #print('invalid Input')
                    continue
                            
crntBalance()                           
                                  
'''
    if other
                    
    


        print('wrong input, reenter')
            continue
        else:
            break
    while True:
        try:
            currency = input('\n Select preffered currency: \n  Ghs \n  Usd')
        except ValueError:
            print('wrong input, select preferred currency')
            continu
        else:
            break
                                      

    
    if "no":
        print("What would you want to do next?")
    else:
        print("invalid input")



    finalquestion = str(input('would you like to make a withdrawal ?  Y/N')
                    
    if finalquestion == 'Y':
                        withdrawalRequest()

    else:
        print('thank you and have a good day')

'''































                        

