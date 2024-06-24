# Basic math operations tutorial 
# Description: Math operations tutorial for Addition, Subtraction, Multiplication and Division with a detailed Report of operations saved locally in userfiles
# Author: Kevin Richard
# Class Names: Report --> Operations --> Tutorial
# Class functions: findReportFiles, readReport, viewReport, saveReport, menuOptions, random_input_numbers, number_of_digits, validator, addition, subtraction, multiplication, division, userInput, insertToReport, printReport, number_of_questions
# Variables : name, positiveReinforcers, supportiveReinforcers, questionMessage, lowerLimit, numberOfDigits, upperLimit, userAnswer, count, selectedOperation, no_of_times, reportGenerated, operation, operations_key, operation_dict, Report, number_of_attempts, number_of_correct, correctAnswer, reallyExit, answer, operation_list, writeFile, readFile, fileListDict, fileOption

# importing random module.
import random
import datetime
import os
import re
import ast

class Report():
    # Initialize class for a new user.
    def __init__(self):
        while True: # Get User Name
            self.Name = input("Enter your Name: ")
            self.firstName = self.Name.split()[0]     # to segregate first name of user
            if self.Name !="" :
                break
        print(f'\nHi {self.Name}, this program will help you practice the basic maths operations.')   # Display Description of program and Instructions.
        print('You will have two chances to get the correct answer. Good luck!!')
        self.positiveReinforcers = ('Excellent..!!', 'Very Good..!!', 'Well Done..!!', 'Awesome..!!', 'Good Job..!!', 'Correct..!!')    # Tuples containng the reinforcers.
        self.supportiveReinforcers = ('Nice Try..', 'OOPS!!', 'Not Quite..', 'Seems to be wrong..', 'Sorry..')
        self.operation_dict = {'1':'Addition','2':'Subtraction','3':'Multiplication','4':'Division'}    # initialize Dictionary to store Report Data
        self.report = {}    # dict variable to store operations data before saving.
        self.savePath = 'C:/Users/kevr0/OneDrive/Desktop/TutorialReports/'  # File save location
        input('\nPress Enter to Begin!!')
    
    # get all user Inputs for Exception handling of ValueError
    def userInput(self,questionMessage,type):
        while True:
            try:
                if type == 'operation':
                    userAnswer=float(input(questionMessage))
                elif type == 'int':
                    userAnswer=int(input(questionMessage))
                return userAnswer
            except ValueError:
                print('\nAnswer is not in a valid data format')
                continue  
    
    # Function to insert data into Report dictionary
    def insertToReport(self,operation,answer):
        if self.report.get(operation) == None : # Operation performed for first time
            number_of_attempts = 1
            if answer:
                number_of_correct = 1
            else:
                number_of_correct = 0
            self.report.update({operation:[number_of_attempts,number_of_correct]})  #Update the report
        else:   # Operation already performed atleast once
            operation_list=self.report.get(operation)
            number_of_attempts = operation_list[0] + 1
            number_of_correct = operation_list[1]
            if answer:
                number_of_correct = operation_list[1] + 1
            self.report.update({operation:[number_of_attempts,number_of_correct]})
        return
    
    # finds all the users save files.
    def findReportFiles(self):
        fileRegex = re.compile(f'{self.firstName}[0-9]+_data.txt|{self.firstName}_data.txt')    # regex to find the user files
        fileListDict = {}
        count = 0
        for _, _, files in os.walk(self.savePath):  # save inormation as dict, so other functions can use data easily.
            for file in files:
                if fileRegex.match(file):
                    count +=1
                    fileListDict.update({count:file})
        return fileListDict,count
    
    # function to save the report data.   
    def saveReport(self):        
        if ( len(self.report.keys()) == 0):
            print('\nNo operations performed to save!! returning back to menu.')
            return
        timeNow = datetime.datetime.now().strftime("%c")
        #referenceNumber = datetime.datetime.now().strftime("%d%m%y%H%M")
        fileListDict,count = self.findReportFiles()
        fileReport = {}
        #fileKeys = list(fileListDict.keys())
        if count == 0:  # if no files exist
            print(f'\nThe report data will be saved in: {self.savePath}{self.firstName}_data.txt')
            #fileReport = {referenceNumber:[timeNow,self.report]}
            fileReport = {timeNow:self.report}
            with open (f'{self.savePath}{self.firstName}_data.txt','w') as writeFile:
                writeFile.writelines(str(fileReport))
        else:
            print('\nChoose file to save to:')  # request user to choose which file to save the data to.
            for fileOption in list(fileListDict.keys()):
                print(f'{fileOption}.\t{fileListDict.get(fileOption)}')
            print(f'{count+1}.\tCreate new file')
            while True:
                fileChoice = self.userInput(':','int')
                if fileChoice <=count: # saves data to file chosen by user.
                    filename = fileListDict.get(fileChoice)
                    fileReport = self.readReport(filename)  # reads the file and stores data as dict to variable
                    fileReport.update({timeNow:self.report})    # appends new data to variable
                    with open (f'{self.savePath}{filename}','w') as writeFile:  # overwrites file with the old and new data
                        writeFile.writelines(str(fileReport))
                    break
                elif fileChoice ==count + 1: # Saves data to a new file.
                    filename = f'{self.firstName}{count+1}_data.txt'
                    fileReport = {timeNow:self.report}
                    with open (f'{self.savePath}{filename}','w') as writeFile:
                        writeFile.writelines(str(fileReport))
                    break
                else:
                    print('\nInvalid option!!. Please re-enter')
            print(f'\nThe report data will be saved in: {filename}')                     
        self.report = {}    # Clears the report variable as information has been saved to file
        return                
  
    # reads the data file and stores it as a dictionary         
    def readReport(self,fileName):
        fileReport = {}
        with open (f'{self.savePath}{fileName}','r') as readFile:
            fileReport = ast.literal_eval(readFile.read())
        return fileReport
            
    # gets user input for report file to display and displays it as meaningfull information
    def viewReport(self):
        fileListDict,count = self.findReportFiles() # checks if files exist for the User
        if(count == 0): # exits if no saved files found for the user
            print('\nThere are no saved files to View!!')
            return
        if(count == 1): # if only one file found, reads it
            fileChoice =1
        else: # if more than one file present, asks user input for which file to display
            print('\nChoose Report file to read:')
            for fileOption in list(fileListDict.keys()):
                print(f'{fileOption}.\t{fileListDict.get(fileOption)}')
            while True:
                fileChoice = self.userInput(':','int')
                if fileChoice <= count:
                    break
                else:
                    print('\nInvalid option!! please re-enter')
        fileReport=self.readReport(fileListDict.get(fileChoice)) # reads and stores the data in selected file to fileReport variable as dict
        print(f'\nHi {self.Name}!!\nReport of Tutotrial')
        print('---------------------------------')
        for time_key in list(fileReport.keys()): # Prints the file data as meaningfull information
            print('\n'+time_key)
            for operation_key in list(fileReport.get(time_key).keys()):
                for operation in operation_key:
                    print(f'\n\tMath Operation : {self.operation_dict.get(operation)}')
                    print(f'\tQuestions attempted = {fileReport.get(time_key).get(operation)[0]}')
                    print(f'\tCorrect Responses = {fileReport.get(time_key).get(operation)[1]}')
                    print(f'\tIncorrect Responses = {fileReport.get(time_key).get(operation)[0] - fileReport.get(time_key).get(operation)[1]}')
            print('      ---------------------------------')
        return

# Operations Class : consists of addition, subtraction, multiplication, division and user answer validator functions
class Operations(Report):
    # Function for validating and assigning reinforcers for user answers.
    def validator(self,userAnswer,correctAnswer):
        if(userAnswer == correctAnswer):    # Verify user answers with correct answers and return.
            print(random.choice(self.positiveReinforcers))  # prints a random positive Reinforcer.
            answer = True
        else:
            print(random.choice(self.supportiveReinforcers))    # prints a random supportive Reinforcer.
            answer = False
        return answer
    
    # Addition function.
    def addition(self, selectedOperation, firstNumber, secondNumber):
        count=0
        while(count<2): # Loop allows the user two chances to get correct answer.
            questionMessage= (f'\nEnter the Sum of: {firstNumber} + {secondNumber} = ') # User Question prompt.
            userAnswer=self.userInput(questionMessage,'operation')            
            correctAnswer=firstNumber + secondNumber
            answer=self.validator(userAnswer,correctAnswer) # Calls validator function to validate answer and print reinforcers message.
            if(answer==True):
                self.insertToReport(selectedOperation,answer)   #insert to report
                return
            count= count + 1
        self.insertToReport(selectedOperation,answer)   #insert to report
        print(f'\nThe correct Answer is {correctAnswer}')   # Print correct answer after two attempts.
        return

    # Subtraction function.
    def subtraction(self, selectedOperation, firstNumber, secondNumber):
        if secondNumber > firstNumber:  # Exchanges values such that firstNumber is a bigger value to prevent negative answers when subtracting.
            firstNumber, secondNumber = secondNumber, firstNumber
        count=0      
        while(count<2): # Loop allows the user two chances to get correct answer.
            questionMessage= (f'\nEnter the Difference of: {firstNumber} - {secondNumber} = ')  # User Question prompt.
            userAnswer=self.userInput(questionMessage,'operation')
            correctAnswer=firstNumber - secondNumber
            answer=self.validator(userAnswer,correctAnswer) # Calls validator function to validate answer and print reinforcers message.
            if(answer==True):
                self.insertToReport(selectedOperation,answer)   #insert to report
                return
            count= count + 1
        self.insertToReport(selectedOperation,answer)   #insert to report
        print(f'The correct Answer is {correctAnswer}') # Print correct answer after two attempts.
        return

    # Multiplication function.
    def multiplication(self, selectedOperation, firstNumber, secondNumber):
        count=0
        while(count<2): # Loop allows the user two chances to get correct answer.
            questionMessage= (f'\nEnter the Product of: {firstNumber} * {secondNumber} = ') # User Question prompt.
            userAnswer=self.userInput(questionMessage,'operation')
            correctAnswer=firstNumber*secondNumber
            answer=self.validator(userAnswer,correctAnswer) # Calls validator function to validate answer and print reinforcers message.
            if(answer==True):
                self.insertToReport(selectedOperation,answer)   #insert to report
                return
            count= count + 1        
        self.insertToReport(selectedOperation,answer)   #insert to report
        print(f'The correct Answer is {correctAnswer}') # Print correct answer after two attempts.
        return

    # Division function.
    def division(self, selectedOperation, firstNumber, secondNumber):
        if secondNumber > firstNumber:  # Exchanges values such that firstNumber is a bigger value to prevent answers less than 1 when dividing.
            firstNumber, secondNumber = secondNumber, firstNumber
        count=0
        print('\n[Rounding example 1) 1.335=1.34  2) 1.337=1.34  3) 1.334=1.33 ]\n')    # Example for rounding
        while(count<2): # Loop allows the user two chances to get correct answer.
            questionMessage= (f'\nDivide and Enter answer ROUNDED upto two decimals: {firstNumber} / {secondNumber} = ')     # User Question prompt.
            userAnswer=self.userInput(questionMessage,'operation')
            correctAnswer=firstNumber/secondNumber
            correctAnswer=round(correctAnswer,2)
            answer=self.validator(userAnswer,correctAnswer) # Calls validator function to validate answer and print reinforcers message.
            if(answer==True):
                self.insertToReport(selectedOperation,answer)   #insert to report
                return
            count= count + 1
        self.insertToReport(selectedOperation,answer)   #insert to report
        print(f'\nThe correct Answer is {correctAnswer}')   # Print the correct answer and return to Menu.
        return

# Tutorial Class: consists the usermenu and operation prompt functions.
class Tutorial(Operations):
     
    # Function to call the menu options and call related functions.
    def menuOptions(self):
        reportGenerated = True
        while(True):    # Menu loop valid until user selects the Exit option and exitFlag=True.
            selectedOperation=input("\nSelect operation to pracitice:-\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Write a Report\n6 - View Report\n7 - Exit\n:")    # request user option.
            if selectedOperation in ('1','2','3','4'):
                reportGenerated = False
                lowerLimit,upperLimit = self.number_of_digits() # call function to get number of digits.
                no_of_times = self.number_of_questions()    # Call function to get number of questions.
                for _ in range(no_of_times):
                    inputValues=self.random_input_numbers(lowerLimit,upperLimit)    # Call function to get two random numbers.           
                    if(selectedOperation=='1'): # Call specific operation functions
                        self.addition(selectedOperation,inputValues[0],inputValues[1])
                    elif(selectedOperation=='2'):
                        self.subtraction(selectedOperation,inputValues[0],inputValues[1])
                    elif(selectedOperation=='3'):
                        self.multiplication(selectedOperation,inputValues[0],inputValues[1])
                    elif(selectedOperation=='4'):
                        self.division(selectedOperation,inputValues[0],inputValues[1])
            elif(selectedOperation=='5'):   # Call function to save Report
                reportGenerated = True
                self.saveReport()
            elif(selectedOperation=='6'):   # Call function to read Reports
                self.viewReport()
            elif(selectedOperation=='7'):
                if not reportGenerated: # Exit will not ask promt if no operations performed after Report was last Generated.
                    reallyExit= input('\nLatest Report not saved and wont be saved if you Exit.. Enter [ Y ] if u want to Exit?')
                    if reallyExit.lower() == 'y':
                        break
                else:
                    break
            else:
                print('Please check entered value !!')
            input('\nPress Enter to continue!!')
        print(f"\nThank You {self.Name}!!") # Exit message when user chooses the exit option.
        return
    
    # User input and exception handling for asking number of questions.
    def number_of_questions(self):
        questionMessage=('\nHow many times would you like to practice the operation?\n:')
        no_of_times = self.userInput(questionMessage,'int')
        return no_of_times

    # Function to get number of digits and return two random Integers.
    def number_of_digits(self):
        while(True):
            numberOfDigits=input('\nWould you like to calculate single or double digit numbers?\n1) Single digits\n2) Double digits\n:') # User input to choose single or double digit numbers.
            if(numberOfDigits == '1'):
                lowerLimit,upperLimit=1,9
                break
            elif(numberOfDigits == '2'):
                lowerLimit,upperLimit=10,99
                break
            else:
                print('Enter valid option 1 or 2 !!')
        return lowerLimit,upperLimit    # call function to return two random numbers as list.

    # Random Input value generator function.
    def random_input_numbers(self,lowerLimit,upperLimit): 
        return [random.randint(lowerLimit,upperLimit),random.randint(lowerLimit,upperLimit)]    # return two random numbers in a List.
     
# main Function
def main():
    newUser1=Tutorial() # Initialize object for Tutorial class.
    newUser1.menuOptions()  # Call menu Options functions for first User.

# main function call
if __name__ == '__main__':
    main()