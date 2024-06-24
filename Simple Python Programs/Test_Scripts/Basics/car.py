
startCar=False
stopCar=True
quitProg=False

print("Type 'help' and press enter for instructions")
while (not quitProg):
    x=str(input("\nEnter the instruction: "))
    if(x=="help"):
        print("start -> Starts the car\nstop -> Stops the car\nquit -> Exit the program")
    elif(x=="start"):
        if(startCar):
            print("The car is already runnning")    
        else:    
            startCar=True
            stopCar=False
            print("The car has started and is running now")
    elif(x=="stop"):
        if(stopCar):
            print("The car is already stopped")    
        else:    
            startCar=False
            stopCar=True
            print("The car has stopped running now")
    elif(x=="quit"):
        print("Exiting the program")
        quitProg=True
        break
    else:
        print("Can not understand, please check case and help")