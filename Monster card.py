myfile = open ("monsters.txt", "r")
mainmenu = ("""
-----------------------------------------

Enter the number of your choice...
1. Display contents of the monster.txt
2. Find if a monster exists
3. Create your own monster card
4. Quit

-----------------------------------------""")

def monstercard():
    print ("Enter the name of your monster")
    Mname = str(input(" "))
    print ("Write the origin story of your monster here")
    origin = str(input(" "))
    print ("Write a description of your monster here")
    desc = str(input(" "))
    print ("Enter your desired attack power (from 0-30)")
    attack = int(input(" "))
    if attack > 30:
        print ("That value is too high!")
        badcount = 1
        while badcount == 1:
            attack = int(input(" "))
            if attack <= 30:
                badcount = 0
                if badcount == 1:
                    print ("That value is still too high!")

    mdef = int(input(" "))
    if mdef > 30:
         print ("That value is too high!")
         badcount = 1
         while badcount == 1:
             mdef = int(input(" "))
             if attack <= 30:
                badcount = 0
             if badcount == 1:
                print ("That value is still too high!")
    mfrce = int(input(" "))
    if mfrce > 30:
        print ("That value is too high!")
        badcount = 1
        while badcount == 1:
            mfrce = int(input(" "))
            if attack <= 30:
                badcount = 0
            if badcount == 1:
                print ("That value is still too high!")
    defence = int(input(" "))
    if defense > 30:
        print ("That value is too high!")
        badcount = 1
        while badcount == 1:
            defense = int(input(" "))
            if attack <= 30:
                badcount = 0
            if badcount == 1:
                print ("That value is still too high!")
                

print (mainmenu)
menuchoice = input (" ")
if menuchoice == "1":
    myfile = open('Monsters.txt','r')
    for line in myfile:
        print(line)
    print (mainmenu)
    menuchoice = input(" ")
if menuchoice  == "2":
    myfile = open("Monsters.txt",'r')
    found = False
    print ("Type in the name of the specific monster to see if its in the database")
    search = input(" ")
    for line in myfile:
        Monster = line.split(",")
        if search in Monster:
            found = True
            print (search, "exists!")
    if found == False:
        print(search, "doesn't exist...")
if menuchoice == "3":
    monstercard()
if menuchoice == "4":
    print ("Saiyonara!")
    quit()
    


