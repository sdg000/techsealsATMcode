#!/usr/bin/env python3
import getpass
import random


print ('########################################### TECH SEALS BANK #####################################################\n')
print ('Please enter your credentials  to login \n')



#Database of user accounts
userArray=[
{'username':'akosua', 'pin':4000, 'balance':{'GHS':140, 'USD':0} },
{'username':'eben', 'pin':5461, 'balance':{'GHS':140, 'USD':0} },
{'username':'bagna', 'pin':7438, 'balance':{'GHS':555000.00, 'USD':300000.00} },
{]


        
def atmMenu():
    print ('Please Pick an option ')


    
#Defining login function an
def userLogin(usern):
    
    for userdata in userArray:
         sessiondata = {'username':'unknown', 'pin':0000, 'balance':{'GHS':0, 'USD':0} } 
    
        #Checks for user existence and says a welcome message

         if usern == userdata['username']    :
            found = True
            sessiondata = userdata #Transfers the found users bank info in to sessiondata variable
            print ("########################################### Welcome to TECH SEALS BANK ATM " , usern, "#####################################################\n")
            print ("Enter your pin to proceed ")
            break
            
            
            
            
         elif usern != userdata['username'] :
            pass
            found = False
            

            
            

    
         
        
            
        
         
        
    return sessiondata #Returns the value of sessiondata after userLogin() is run,  so we can use in the continuing code 



    
def pinverify(userpin):
    valid = False
    pin = str(getpass.getpass("Enter your pin: \n"))
    
    if userpin == pin :
        valid = True
        
    return valid

#User has to enter the name
usern = input("Username: ")

usern = usern.lower()
#loginpin = str(getpass.getpass("Enter your pin: \n"))

session=userLogin(usern)

#the user's Pin from data dictionary
userpin = str(session['pin'])

bala = session['balance']

#Cedis Balance
ghbal = float(bala['GHS'])

#Dollar Balance
usbal = float(bala['USD'])



if pinverify(userpin) == True :
    atmMenu()

else:
    
    print("   You have entered an Invalid Login.  ")







