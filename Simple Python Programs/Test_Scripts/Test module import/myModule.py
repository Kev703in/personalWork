
# addition module for two inputs
def addition(first_number, second_number):
    return first_number+second_number
    
# subtraction module for two inputs
def subtraction(first_number, second_number):
    return first_number-second_number

#Prime number checker for one input
def primeNumber(number):
    if(number==2):
        return True
    if(number>1):
        for n in range(2,number):
            if (number%n==0 ):
                return False
        return True
    else:
        return False