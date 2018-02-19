def Start():
    decision = input ("Do you want to run the 'counter' or the 'simple script?'")
    if decision == "Counter" or decision == "counter" or decision == "COUNTER":
        Counter()
    if decision == "Simple script" or decision == "Simple Script" or decision == "SIMPLE SCRIPT" or decision == "simple script":
        Simple()

def Restart():
    Restart = input ("Do you want to restart the program? Y/N")
    if Restart == "Y" or Restart == "y":
        print ("Restarting...")
        Start()
    if Restart == "N" or Restart == "n":
        print ("Goodbye :[")
        quit
        
def ResetC():
    Redo = input ("Do you want to reload the Counter? Y/N")
    if Redo == "Y" or Redo == "y":
        print ("Reloading...")
        Counter()
    if Redo == "N" or Redo == "n":
        Restart()


def ResetSi():
    Redo = input ("Do you want to reload the Simple script? Y/N")
    if Redo == "Y" or Redo == "y":
        print ("Reloading...")
        Simple()
    if Redo == "N" or Redo == "n":
        Restart()


def Counter():
    option = input ("Count NORMALLY, in EVEN, in ODD numbers, or in TENS from 0 to 100?")

    if option == "EVEN" or option =="even" or option =="Even":
        for i in range (0,101,2):print(i)
    
    if option == "ODD" or option =="odd" or option == "Odd":
        for i in range (1,101,2):
            print(i)
    
    if option == "TENS" or option == "tens" or option == "Tens":
        for i in range (0,101,10):
            print (i)
    
    if option == "NORMALLY" or option =="normally" or option == "Normally":
        for i in range (0,101):
            print(i)
    print("Done!")
    ResetC()
       
        
def Simple():
    name = input ("Hello there! What's your name?")
    print ("Hello",name)
    ResetSi()

Start()




#WIP CODE --------------------------------

#def Txtadventure():
    #Hp = 100
    #Gold = 0
    #Exp = 0
#print ("Do you recall your name?")





    






            
                
    
