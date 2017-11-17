import random
numgen = random.Random()
number = numgen.randrange(1, 100)
#print (number) #To test if num re-generates if it lands on 25,50 or 75.
while number == 50 or number ==75 or number==25:
    number = numgen.randrange(1, 100)
#print (number) #debug



def win():
    input ("\n\nGreat, you got it with {0} Lives remaining!\n\n".format(Lives))


def predictiongame():
    global predict
    global msg
    global Lives
    global number
    global Difficulty
    predict = int(input(msg + """\nI have a number between 1 and 100
Try to guess it!: """))
    if predict > number:
        msg += str(predict) + " is higher than my number.\n"
        Lives -=1
        print (Lives, """Lives left
----------------------------------------------------------""")
    if predict < number:
        Lives -= 1
        msg += str(predict) + " is lower than my number.\n"
        print (Lives, """Lives left
----------------------------------------------------------""")
    if Lives == 0:
        msg = ""
        print ("Game over man, game over!")
        retry = input("""Do you want to try again?
Y/N""")
        if retry == ("Y") or retry == ("y"):
             print ("Restarting...")
             predictiongame()
        if retry == ("N") or retry == ("n"):
            print ("Goodbye!")
            quit()
    if predict == number:
         win()

def hints():        
    while True:
        global number
        if number > 50:
            print ("The number is greater than 50")
            if number < 75:
                print ("But it is also less than 75")
            if number > 75: ("But it is also greater than 75")
            predictiongame()
        elif number < 50:
            print ("The number is less than 50")
            if number < 25:
                print ("But it is also less than 25")
            if number > 25:
                print ("But it is also greater than 25")
            predictiongame()

msg = ""    
Difficulty = input("""Select your difficulty
1)Normal
2)Hard
3)Insane""")
if Difficulty == "Normal" or Difficulty == "normal":
    Lives = 5
    print ("Have fun!")
    hints()
if Difficulty == "Hard" or Difficulty == "hard":
    Lives = 10
    print ("Good luck...")
    predictiongame()

