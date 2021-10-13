
def atmMenu(): 
    print('Welcome to techSeals Bank')
    print('Please select an option below')
    print ('1. Withdrawal')
    print ('2. Check Balance')
    print ("3. Add-Ons")
    print ('4. Log Out/Quit')
    choice = str(input('Please enter your choice (1, 2, 3 or 4): '))

    if choice == '1':
        withdrawUpdate()
    
    elif choice == '2':
        crntBalance()

    elif choice == '3':
        addOns()
    
    elif choice == '4':
        exit()
    
    else: 
        print('Sorry your choice is invalid')
        atmMenu()













