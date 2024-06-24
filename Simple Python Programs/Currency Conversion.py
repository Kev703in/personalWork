# Currency conversion 
# Description: USD to Pounds and vise versa
# Author: Kevin Richard
# Input Variables: userNAme, conversionLoop, selectConversion, USD_Inputvalue, Pounds_Inputvalue
# Output Variables: USDinPounds, PoundsinUSD

class CurrencyConversion():

    def __init__(self):
        self.userNAme=self.getUsername()
        self.conversionLoop='y' 
    
    def getUsername(self): #Requesting Name
        return input("Enter your Name: ")

    def USDToBPound(self): #Convert from USD to Pounds and return
        USD_Inputvalue=int(input("\nEnter amount in USD: "))
        USDinPounds=USD_Inputvalue*0.87
        return USDinPounds

    def BpoundToUSD(self): #Convert form Pounds to USD and return
        Pounds_Inputvalue=int(input("\nEnter amount in Pound Sterling: "))
        PoundsinUSD=Pounds_Inputvalue*1.15
        return PoundsinUSD

    def conversionModule(self): #Show conversion options, get selected option 
        try:
            selectConversion = int(input("\nEnter your Choice -> \n1 – Convert US Dollar to British Pound\n2 – Convert British Pound to US Dollar\n3 – Exit\n:"))
            if(selectConversion==1): # Convertion of currency value (Selection control structure)
                print(f'The value is {self.USDToBPound()} £')
            elif(selectConversion==2):
                print(f'The value is {self.BpoundToUSD()} $')
            elif(selectConversion==3):
                return "Exit"
            else:
                print('\nWrong option selected... PLease try again')    
        except ValueError:
            print(f"The entered value is not an integer.")

def main():
    instance = CurrencyConversion()
    while(instance.conversionLoop[0]=='y'or instance.conversionLoop[0]=='Y'): # Check if User wants to convert again(Repetition control Structure) 
        status=instance.conversionModule()
        if(status=="Exit"):
            break
        instance.conversionLoop=input("\nDo you want to continue? [Type yes or no]: ")

    print(f'\nThank you {instance.userNAme}')
    print("Exiting Program!!!")


if __name__ == "__main__":
    main()