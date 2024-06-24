# Body Mass Index calculation with relevant messages
# Description: BMI value and notify general condition 
# Author: Kevin Richard 
# Input Variables: userName, measurementFlag, userHeight, userWeight
# Output Variables: BMI, conditionMessage, userName

import sys
# Requesting Name
userName = input("Please Enter your Name: ")
# Requesting Measurement System
measurementFlag = input("Choose measurement system \n 1) Metric System (Height in cm, Weight in kg) \n 2) Imperial System (Height in feet, Weight in lb) \n:")
# Check if correct option selected for Measurement System
if(measurementFlag != "1" and measurementFlag != "2"):
    print("Please enter either option '1' for metric or option '2' for Imperial System. \n**** Terminateing Program ****")
    sys.exit()

# Requesting Height and Weight
userHeight= float(input("\nEnter your Height: "))
userWeight= float(input("Enter your Weight: "))

# Calculate BMI (changes in formula is to account for cm to m && feet to inch conversion )
if(measurementFlag == "1"):
    BMI= (userWeight*10000)/(userHeight**2)
elif(measurementFlag =="2"):
    BMI = (userWeight*703)/((userHeight**2)*12*12)

# Output messages
if(BMI>24.6):
    conditionMessage=" Your BMI is too High!! Please check with a Doctor, you might require Medical Attention."
elif(BMI<18.4):
    conditionMessage=" Your BMI is too Low!! Please check with a Doctor, you might require Medical Attention."
elif(BMI>23.6):
    conditionMessage=" Your BMI is in the Healthy bracket, But it's time for a RUN!!"
else:
    conditionMessage=" Your BMI is in the Healthy bracket."

print(f"\nHi {userName}!! Your BMI Value is {BMI}\n\n{conditionMessage}")
print("(Healthy range for BMI is roughly between 18.5 to 24.5)")