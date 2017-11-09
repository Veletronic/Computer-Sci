import turtle
wi = int(input ("What width do you want your window to be?") )
he = int(input ("What height do you want your window to be?") )
turtle.setup(wi, he)
wn = turtle.Screen()
wn.title("Handling keypresses!")
colorbg = input("What background color do you want?")
wn.bgcolor(colorbg)
nally = turtle.Turtle()
colorpen= input ("What color do you want to draw in?")
nally.color(colorpen)
pensz= input ("How large do you want the pensize to be? (Number)")
nally.pensize(pensz)

instructions = ("""
UP KEY = FORWARD
DOWN KEY = BACKWARDS
LEFT KEY = ROTATE LEFT
RIGHT KEY = ROTATE RIGHT
Q = CLOSE TURTLE
W = STOP DRAWING
S = START DRAWING""")

print (instructions)

def k1():
    nally.forward(30)
def k2():
    nally.left(45)
def k3():
    nally.right(45)
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
def k7():
    nally.pendown()




wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3,"Right")
wn.onkey(k4, "Down")
wn.onkey(k5, "q")
wn.onkey(k6, "w")
wn.onkey(k7, "s")

wn.listen()
wn.mainloop()
       
