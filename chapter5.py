import turtle
Decisioncount = 0
def draw_bar(t, height):
    t.begin_fill()           
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             
    t.forward(10)

wn = turtle.Screen()         
wn.bgcolor("lightgreen")

Ryan = turtle.Turtle()       
Ryan.color("blue", "red")
Ryan.pensize(3)
Ryan.penup()
Ryan.right(90)
Ryan.forward(395)
Ryan.left(90)
Ryan.pendown()

def MoreInp():
    global Decisioncount
    global input5
    Decision = input ("""Do you want to add another value?
Y/N""")
    if Decision == ("Y") or Decision == ("y"):
        Decisioncount = 1
        input5 = int(input("Input your fifth value here"))
        MoreInp2()
    if Decision == ("N") or Decision == ("n"):
        Bargraph()

def MoreInp2():
    global Decisioncount
    global input6
    Decision2 = input ("""Do you want to add another value?
(Y/N)""")
    if Decision2 == ("Y") or Decision2 == ("y"):
         input6 = int(input("Input your sixth value here"))
         Decisioncount = 2
         Bargraph()
    if Decision2 == ("N") or Decision2 == ("n"):
        Bargraph()
    
def Bargraph():
    if Decisioncount == 0:
        xs = [input1, input2, input3, input4]
    if Decisioncount == 1:
        xs = [input1, input2, input3, input4, input5]
    if Decisioncount == 2:
        xs = [input1, input2, input3, input4, input5, input6]   
    for a in xs:
        draw_bar(Ryan, a)

input1 = int(input("Insert your first value here"))
input2 = int(input("Insert your second value here"))
input3 = int(input("Insert your third value here"))
input4 = int(input("Insert your fourth value here"))
MoreInp()

wn.mainloop()
