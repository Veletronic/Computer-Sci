import random
Lives = 0
Diffselected = 0

def mainmenu(): #Main menu module
    global Diffselected #Allows this var from difmenu() to be retrieved
    start = 0
    while start == 0:
        Userinput = int(input("""MAIN MENU

    1.PLAY GAME
    2.SELECT DIFFICULTY
    3.EXIT
    """))
        if Userinput == 1:
            if Diffselected == 1:
                print ("Starting game...")
                start = 1
                maingame()
            else:
                print ("Hey! You gotta select a difficulty first!")
        if Userinput == 2:
            difmenu()

def difmenu(): #Can be turned into a case statement for pseudocode
    global Lives
    global Diffselected
    global rng
    Diffselected = 1
    Userinput2 = int(input("""Difficulty Select
    1.Easy
    2.Normal
    3.Hard
    4.Heroic
    5.Legendary
    6.Insanity

    """))
    if Userinput2 == 1: 
        rng = 10 #Sets how high the range is (e.g in range(0,rng))
        Lives = 10
        print ("You have selected easy, mommy let you on her computer for the first time??")
    if Userinput2 == 2:
        rng = 50
        Lives = 5
        print ("You have selected Normal, what a normie.")
    if Userinput2 == 3:
        rng = 100
        Lives = 3
        print ("You have selected Hard, you must be up for a challenge!")
    if Userinput2 == 4:
        rng = 500
        Lives = 3
        print ("You have selected heroic, but are you really though?")
    if Userinput2 == 5:
        rng = 1000
        Lives = 3
        print ("You have selected legendary, god speed to you...")
    if Userinput2 == 6:
        rng = 5000
        Lives = 3
        print ("Insane in the membrane, insane in the brain!")

def maingame():
    global Lives
    global rng
    ScoreMult = 1
    streak = 0
    Streakcount = 0
    print ("""Welcome to the game...
           numbers generated within this difficulty are between 0 and""", rng)
    score = 0
    
    while Lives !=0:
        Num = random.randrange(0,rng)
        #print(Num) Used for debugging, or you can use it to cheat ;)
        Guess = int(input("""
        Enter your guess here: """))
        if Guess == Num:
            score = (score + 1) * ScoreMult
            streak = streak + 1 #This streak is purely to trigger the multiplier
            Streakcount = Streakcount + 1 #This streakcount is to allow the user to see his streaks
            print ("Current streak: ", Streakcount)
            if streak == 5: #Streak resets upon reaching 5, gives the player a life and increases score multiplier.
                ScoreMult = ScoreMult + 1
                Lives = Lives + 1
                streak = streak - 5
                print ("Score multiplier has increased to", ScoreMult, "and you have gained a life! Your current amount of lives is:",Lives)
            print ("Current score: ", score)
        if Guess > Num:
            streak = 0
            Lives = Lives - 1
            HighestStreak = Streakcount #Stores the highest streak before resetting
            Streakcount = 0
            print ("My number is less than that, you have", Lives, "lives remaining.")
        if Guess < Num:
            streak = 0
            Lives = Lives - 1
            HighestStreak = Streakcount
            Streakcount = 0
            print ("My number is greater than that, you have", Lives, "lives remaining.")
    if Lives == 0:
        print ("Game over man!")
        print ("You have scored", score, "points in total!")
        print ("Your highest streak was", HighestStreak)
        Gmenu()

def Gmenu():
    choice = 0
    Annoyed = 0
    while choice == 0:
        Gmenu = input("""
    1.Return to main menu
    2.Exit
    """)
        if Gmenu == ("1"):
            print("Returning to main menu. . .")
            Choice = 1
            mainmenu() #Program crashes after selecting this then starting the game, don't know how to fix yet.
        if Gmenu == ("2"):
            Confirm = int(input("""Are you sure?
                1.Yes
                2.No
                """))
            if Confirm == 1:
                    quit()
            if Confirm ==2:
                if Annoyed !=8:
                    print ("Make up your mind!")
                Annoyed = Annoyed + 1
                if Annoyed >8:
                    print ("*Silence...*")
            else:
                Annoyed = Annoyed + 1
                if Annoyed == 1:
                    print ("Uh...could you repeat that?")
                if Annoyed == 2:
                    print ("I'm sorry, what?")
                if Annoyed == 3:
                    print ("Look, the menu is simple, you just input the number next to the option, it isn't that hard.")
                if Annoyed == 4:
                    print ("Oh now you're just trying to waste my time.")
                if Annoyed == 5:
                    print ("What do you think you're going to gain from this??")
                if Annoyed == 6:
                    print ("I bite my thumb at thee!")
                if Annoyed == 7:
                    print ("Can you STOP wasting both of our time and just pick an actual option.")
                if Annoyed == 8:
                    print ("Alright, I'm gonna go catch up on some netflix series, have fun being a numpty.")
                if Annoyed > 8:
                    print ("*No one responds...*")
                
            
                          
            
            
