import turtle
wi = int(input ("What width do you want your window to be?") )
he = int(input ("What height do you want your window to be?") )
turtle.setup(wi, he)
wn = turtle.Screen()
wn.title("Draw pad!")
colorbg = input("What background color do you want?")
wn.bgcolor(colorbg)
nally = turtle.Turtle()
colorpen= input ("What color do you want to draw in?")
nally.color(colorpen)
pensz= input ("How large do you want the pensize to be? (Number)")
nally.pensize(pensz)
pochexist = 0

def createpoch():
    global pensz
    global colorpen
    pochi = turtle.Turtle()
    pochi.color(colorpen)
    pochi.pensize(pensz)
    pochexist = 1

instructions = ("""
UP KEY = FORWARD
DOWN KEY = BACKWARDS
LEFT KEY = ROTATE LEFT
RIGHT KEY = ROTATE RIGHT
q = CLOSE TURTLE
w = STOP DRAWING
s = START DRAWING
c = CHANGE COLOR
r = CHANGE RESOLUTION
p = CHANGE PEN WIDTH
b = CHANGE BG COLOR
d = CHANGE DRAW SPEED
o = RE-CENTER THE CURSOR
DELETE = CLEAR SCREEN
h = HIDE CURSOR
v = UNHIDE CURSOR
Make sure capslock is off!""")

print (instructions)

def drawspd():
    drawspeed = input ("""Choose your drawing speed:
1.Fast
2.Medium
3.Slow (This option is slightly buggy, try not to mash the arrow keys)
""")
    if drawspeed == "Fast" or drawspeed == "fast":
        print ("Drawing speed is set to FAST")
        nally.speed(10)
    if drawspeed == "Medium" or drawspeed == "medium":
        print ("Drawing speed is set to MEDIUM")
        nally.speed(5)
    if drawspeed == "Slow" or drawspeed == "slow":
        print ("Drawing speed is set to SLOW")
        nally.speed(1)

def k1():
    nally.forward(30)
    if pochexist == 1:
        pochi.backward(30)
def k2():
    nally.left(45)
    if pochexist == 1:
        pochi.right(45)
def k3():
    nally.right(45)
    if pochexist == 1:
        pochi.left(45)
def k4():
    nally.backward(30)
def k5():
    qoption = input("""Are you sure you want to exit?
Y/N?""")
    if qoption == "Y" or qoption == "y":
        print ("Goodbye!")
        wn.bye()
    if qoption == "N" or qoption == "n":
        print ("Oh okay.")
def k6():
    nally.penup()
    print ("NOT DRAWING")
def k7():
    nally.pendown()
    print ("DRAWING")
def k8():
    global colorpen
    colorpen = input ("What do you want to change your color to?")
    nally.color(colorpen)
    print ("The color is now", colorpen)
def k9():
    global pensz
    pensz = input ("what do you want to change your pensize to?")
    nally.pensize(pensz)
    print ("The pensize is now", pensz)
def k10():
    global he
    global wi
    he = int(input ("What do you want to change the height to?"))
    wi = int(input("What do you want to change the width to?"))
    turtle.setup (he, wi)
    print ("The resolutions is now", he, "x", wi)
def k11():
    global colorbg
    colorbg = input("What do you want to change the bg color to?")
    wn.bgcolor(colorbg)
    print ("The bg color is now", colorbg)
def k12():
    nally.clear()
def k13():
    global drawspeed
    drawspd()
def k14():
    nally.hideturtle()
    print ("Cursor is INVISIBLE")
def k15():
    nally.showturtle()
    print ("Cursor is VISIBLE")
def k16():
    nally.penup()
    nally.setx(0)
    nally.sety(0)
    nally.pendown()
    print ("CURSOR RE-CENTERED")

                 





wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3,"Right")
wn.onkey(k4, "Down")
wn.onkey(k5, "q")
wn.onkey(k6, "w")
wn.onkey(k7, "s")
wn.onkey(k8, "c")
wn.onkey(k9, "p")
wn.onkey(k10, "r")
wn.onkey(k11, "b")
wn.onkey(k12, "Delete")
wn.onkey(k13, "d")
wn.onkey(k14, "h")
wn.onkey(k15, "v")
wn.onkey(k16, "o")


wn.listen()
wn.mainloop()
       
