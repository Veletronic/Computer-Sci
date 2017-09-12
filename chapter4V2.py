import turtle
__import__("turtle")._traceable__ = True


def four_sqr():
    for i in range(4):
        glados.color("white")
        square()
        glados.penup()
        glados.forward(22)
        glados.pendown()
    anotherone()


def trippy():
    Color1 = input ("Enter your first color")
    Color2 = input ("Enter your second color")
    Color3 = input ("Enter your third color")
    for x in range(25):
        glados.speed(100)
        for i in [Color1, Color2, Color3]:
            glados.color(i)
            square()
            glados.penup()
            glados.right(5)
            glados.pendown()
    anotherone()

def star():
    angle = 120
    size = 10
    for side in range(5):
        glados.forward(size)
        glados.right(angle)
        glados.forward(size)
        glados.right(72 - angle)

def fivestars():
    glados.color("white")
    for i in range(5):
        star()
        glados.penup()
        glados.right(144)
        glados.forward (350)
        glados.pendown()
    anotherone()

def mult_pattern():
    Color1 = input ("Enter your first color")
    Color2 = input ("Enter your second color")
    Color3 = input ("Enter your third color")
    Color4 = input ("Enter your fourth color")
    global size
    size = 20
    for x in range(50):
        size = size + 5
        glados.speed(50)
        for i in [Color1, Color2, Color3, Color4]:
            glados.speed(25)
            glados.color(i)
            square()
            glados.right(10)
    anotherone()

size=20
          
def square():
    glados.forward(size)
    glados.left(90)
    glados.forward(size)
    glados.left(90)
    glados.forward(size)
    glados.left(90)
    glados.forward(size)

    
def mult_clr_spr(t, sz):
    Color1 = input ("Enter your color choice")
    for i in [Color1]:
        glados.color(i)
        glados.forward(sz)
        glados.left(90)

def draw_mult_clr_spr():
    size = 20
    for i in range(15):
        mult_clr_spr(glados, size)
        size = size + 10
        glados.forward(10)
        glados.right(18)
    anotherone()

glados = turtle.Turtle()
glados.pensize(3)
wn = turtle.Screen()
Bgcolor = input ("Enter your background color choice")
wn.bgcolor(Bgcolor)

def choice():
    userchoice = input("""What do you want to draw?
1)four squares
2)multi-color spiral
3)trippy circle
4)multi-color pattern
5)five stars """)
    if userchoice == ("four squares"):
        four_sqr()
    if userchoice == ("multi-color spiral"):
        draw_mult_clr_spr()
    if userchoice == ("trippy circle"):
        trippy()
    if userchoice == ("multi-color pattern"):
        mult_pattern()
    if userchoice == ("five stars"):
        fivestars()

def anotherone():
    RestartChoice = input("""Do you want to draw another pattern onto the existing canvas?
    Y/N?""")
    if RestartChoice == ("Y") or RestartChoice == ("y"):
        choice()
    if RestartChoice == ("N") or RestartChoice == ("n"):
        print ("Goodbye!")
        exit()

choice()


wn.mainloop()
