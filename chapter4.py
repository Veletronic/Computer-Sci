import turtle
__import__("turtle")._traceable__ = True

def square():
    glados.forward(50)
    glados.left(90)
    glados.forward(50)
    glados.left(90)
    glados.forward(50)
    glados.left(90)
    glados.forward(50)

def four_sqr():
    for i in range(4):
        glados.color("white")
        square()
        glados.penup()
        glados.forward(22)
        glados.pendown()


def trippy():
    Color1 = input ("Enter your first color")
    Color2 = input ("Enter your second color")
    Color3 = input ("Enter your third color")
    for x in range(25):
        for i in [Color1, Color2, Color3]:
            glados.speed(25)
            glados.color(i)
            square()
            glados.penup()
            glados.right(5)
            glados.pendown()

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
    

def mult_pattern():
    Color1 = input ("Enter your first color")
    Color2 = input ("Enter your second color")
    Color3 = input ("Enter your third color")
    size = 20
    for x in range(25):
        size = size + 25  #size isn't increasing here??
        for i in [Color1, Color2, Color3]:
            glados.speed(25)
            glados.color(i)
            square()
            glados.right(10)
    
def mult_clr_sqr(t, sz):
    Color1 = input ("Enter your color choice")
    for i in [Color1]:
        glados.color(i)
        glados.forward(sz)
        glados.left(90)

def draw_mult_clr_sqr():
    size = 20
    for i in range(15):
        mult_clr_sqr(glados, size)
        size = size + 10
        glados.forward(10)
        glados.right(18)

glados = turtle.Turtle()
glados.pensize(3)
wn = turtle.Screen()
Bgcolor = input ("Enter your background color choice")
wn.bgcolor(Bgcolor)

userchoice = input("""What do you want to draw?
1)four squares
2)multi-color squares
3)trippy circle
4)multi-color pattern (not working as intended)
5)five stars """)
if userchoice == ("four squares"):
    four_sqr()
if userchoice == ("multi-color squares"):
    draw_mult_clr_sqr()
if userchoice == ("trippy circle"):
    trippy()
if userchoice == ("multi-color pattern"):
    mult_pattern()
if userchoice == ("five stars"):
    fivestars()




wn.mainloop()
