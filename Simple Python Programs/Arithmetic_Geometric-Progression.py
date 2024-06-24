# Program : GP and AP 
# Description: User prompt for desired progression, AP or GP
# Author: Kevin Richard 
# Input Variables: starting_number, Common_ratio, Nth_term, chosenFunction
# Output Variables: outputOfFunction

def Aritmetic_progression(starting_number,Common_ratio,Nth_term): #Define AP function
    n_value=1
    outputOfFunction=""
    while(n_value<=Nth_term):
        AP = (starting_number+ (n_value-1)*Common_ratio)  # AP Formula
        outputOfFunction+= str(AP) +" "
        n_value +=1
    print(f'\nThe AP for given inputs is:\n{outputOfFunction}')
    return 

def Geometric_progression(starting_number,Common_ratio,Nth_term):   #Define GP function
    n_value=0
    outputOfFunction=""
    while(n_value<Nth_term):
        GP = (starting_number*Common_ratio**n_value)    # GP Formula
        outputOfFunction+= str(GP) +" "
        n_value+=1
    print(f'\nThe GP for given inputs is:\n{outputOfFunction}')
    return

def get_inputs(): #Define function for getting inputs
    starting_number = int(input("Enter the starting number: "))
    Common_ratio = int(input("Enter the common ration(GP) or difference(AP): "))
    Nth_term = int(input("Enter the number of iterations: "))
    return [starting_number,Common_ratio,Nth_term]

def menu_options(): #define menu_options
    chosenFunction = 0  #initialize chosenFunction
    while(chosenFunction != 3):
        #Ask user for function used
        chosenFunction = int(input("\nChoose the function to perform:\n1)Aritmetic_progression\n2)Geometric_progression\n3)Exit\n:"))
        if(chosenFunction==1):
            inputValues = get_inputs()  #call get_inputs function for taking input
            Aritmetic_progression(inputValues[0],inputValues[1],inputValues[2])
        elif(chosenFunction==2):
            inputValues = get_inputs()
            Geometric_progression(inputValues[0],inputValues[1],inputValues[2])
        elif(chosenFunction==3):
            return
        else:
            input("\nWarning!! Please Choose between options 1 to 3\nPress Enter to continue")

menu_options()
print("Exiting The Program!!!")