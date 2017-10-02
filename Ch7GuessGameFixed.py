import random
numgen = random.Random()
number = numgen.randrange(1, 100)
#print (number) #debug

Lives = 5
msg = ""

def win():
    input ("\n\nGreat, you got it with {0} Lives remaining!\n\n".format(Lives))


def predictiongame():
    global predict
    global msg
    global Lives
    global number   
    predict = int(input(msg + """\nI have a number between 1 and 100
Try to guess it!: """))
    if predict > number:
        msg += str(predict) + " is higher than my number.\n"
        Lives -=1
        print (Lives, """Lives left
----------------------------------------------------------""")
    elif predict < number:
        Lives -= 1
        msg += str(predict) + " is lower than my number.\n"
        print (Lives, """Lives left
----------------------------------------------------------""")
    if Lives == 0:
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

def hints():        #Python is ignoring this w/out showing an error?
    while True:
        global number
        if number > 50:
            print ("The number is greater than 50")
            if number < 75:
                print ("But it is less than 75")
            if number > 75: ("But it is greater than 75")
            predictiongame()
        elif number < 50:
            print ("The number is less than 50")
            if number < 25:
                print ("But it is less than 25")
            if number > 25:
                print ("But it is greater than 25")
            predictiongame()

hints() 


