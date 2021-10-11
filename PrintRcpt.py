import random

#ask the clinet if they want a receipt for their transaction or not

loginDetails =["Anne", "10011000"]  #Dummy login details
amtWithdrawn =["GHS200"] #dummy amount withdrawn
currentBalance =["GHS400"] #dummy current balance

def rcptPrint():
    while True:
        optn = input("Do you want a receipt for your transaction?(y/n):")
        if optn == "y":
            print(".........Transaction Receipt............\n")
            print("****************************************\n")
            print("Transaction is now complete.\n")                       
            print("Transaction number: "+str(random.randint(10000,100000000))+"\n")
            print("Account details: "+str(loginDetails[0])+"\n") 
            print("Amount withdrawn: "+str(amtWithdrawn[0])+"\n")      
            print("Available balance: "+str(currentBalance[0])+"\n")                 
            print("Thank you for choosing Tech Seals Bank\n")
            print("*************************************")
            break

        elif optn == "n":
            print("""
                -----------------------------------------
                | Thank you for choosing Tech Seals Bank |
                |         Visit us again!                |
                -----------------------------------------
            """)
            break   
        else:
            print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
            continue

rcptPrint()