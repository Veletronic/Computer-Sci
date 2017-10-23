import random
import fileinput

#with fileinput.input(files=("words.txt")) as f:
    #for line in f:
        #process(line)

life = 5
Guess = ' '
Nolost = 0
gloopcount = 0
correctcount = 0

word = ("massive")
    

def userguess():
    global Guess
    global life
    global Nolost
    global print
    global msg1
    global msg2
    global gloopcount
    msg1 = "Give your first guess"
    msg2 = "You have"
    while life > 0:
        guess()
        print (msg2, life, "lives left")
    if life == 0:
        print ("Game Over")
        Nolost += 1
        msg3 = "You have lost"
        print = (msg3, Nolost, "times")
        retry = input("""Do you want to retry?
Y/N?""")
        if retry == "Y" or retry == "y":
            wordgen()
        if retry == "N" or retry == "n":
            print ("Goodbye")
            quit()


def guess():
    global life
    global Guess
    global gloopcount
    global msg1
    global correctcount
    if len (word) == (correctcount):
        print ("YOU WIN CONGRATS HAHA")
        quit()
    while life == 5:
        Guess = input(msg1)
        gloopcount += 1
        if Guess in word:
            print (Guess, "is one of the letters")
            correctcount +=1
        else:
            life -=1
            print (Guess, "Is not one of the letters, try again")
    if gloopcount >=1:
        msg1 = "Give your next guess."
    if life <= 4:
        gloopcount +=1
        Guess = input(msg1)
        if Guess in word:
            print (Guess, "is one of the letters")
            correctcount +=1
        else:
            life -=1
            print (Guess, "Is not one of the letters, try again")

userguess()
