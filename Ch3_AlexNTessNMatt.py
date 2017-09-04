import turtle
def Triangle():
    tess.forward(80)             # Make tess draw equilateral triangle
    tess.left(120)
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(120)               # Complete the triangle

    tess.right(180)              # Turn tess around
    tess.forward(80)             # Move her away from the origin

def Star():
    for i in range(20):
        tess.forward(i * 10)
        tess.right(144)

def AlSquare():
    alex.forward(50)             # Make alex draw a square
    alex.left(90)
    alex.forward(50)
    alex.left(90)
    alex.forward(50)
    alex.left(90)
    alex.forward(50)
    alex.left(90)

def AlTriangle():
    alex.forward(80)
    alex.left(120)
    alex.forward(80)
    alex.left(120)
    alex.forward(80)
    alex.left(120)
    

wn = turtle.Screen()
ChoicesBG = """Choose your desired background color:
1.Azure
2.Beige
3.Black
4.Blue
5.Brown
6.Chocolate
7.Coral
8.Cyan
9.DarkCyan
10.DarkGray
11.DarkGreen
12.FloralWhite
13.gainsboro
14.GhostWhite
15.Gold
16.Cadetblue
17.Aliceblue"""
Color = input (ChoicesBG)
wn.bgcolor(Color)      #BGColor
wn.title("Tess & Alex & Matt")      #Title

tess = turtle.Turtle()
ChoicesTess = """Choose your desired color for Tess:
1.Azure
2.Beige
3.Black
4.Blue
5.Brown
6.Chocolate
7.Coral
8.Cyan
9.DarkCyan
10.DarkGray
11.DarkGreen
12.FloralWhite
13.gainsboro
14.GhostWhite
15.Gold
16.Cadetblue
17.Aliceblue"""
TessColor = input (ChoicesTess)
tess.color(TessColor)            # Tess's color
PSize = input ("What would you like the pen width to be set to?")
tess.pensize(PSize)               # penwidth
ShapeChoice = """Choose your desired shape to be drawn by Tess:
1.Triangle
2.Star"""
Shape = input (ShapeChoice)
if Shape == ("Star") or Shape == ("star"):
    Star()
if Shape == ("Triangle") or Shape == ("triangle"):
    Triangle()

alex = turtle.Turtle()
AlChoice = """Choose your desired shape to be drawn by Alex:
1.Square
2.Triangle"""
AlShape = input (AlChoice)
if AlShape == ("Square") or AlShape == ("square"):
    AlSquare()
if AlShape == ("Triangle") or AlShape == ("triangle"):
    AlTriangle()

matt = turtle.Turtle()
matt.shape("turtle")
ChoicesMatt = """Choose your desired color for Matt:
1.Azure
2.Beige
3.Black
4.Blue
5.Brown
6.Chocolate
7.Coral
8.Cyan
9.DarkCyan
10.DarkGray
11.DarkGreen
12.FloralWhite
13.gainsboro
14.GhostWhite
15.Gold
16.Cadetblue
17.Aliceblue"""
Mattcolor = input (ChoicesMatt)
matt.color(Mattcolor)

matt.penup()
size = 20
for i in range (30):
    matt.stamp()
    size = size + 3
    matt.forward(size)
    matt.right(24)


wn.mainloop()
