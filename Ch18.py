import turtle



def koch(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def koch_0(t, size):
    t.forward(size)

def koch_1(t, size):
    for angle in [60, -60, 60, 0]:
       koch_0(t, size/3)
       t.left(angle)

def koch_2(t, size):
    for angle in [60, -120, 60, 0]:
       koch_1(t, size/3)
       t.left(angle)

def koch_3(t, size):
    for angle in [60, -120, 60, 0]:
       koch_2(t, size/3)
       t.left(angle)

t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Fractals")
order = int(input("Choose the Order"))
size = int(input("Choose the Size")) #Dev note: Be sure to set the size >100
print ("________________________________________")
H = int(input("Choose your resolution height"))
W =int(input("Choose your resolution width"))
turtle.setup(H, W)
Tcolour = input("Choose your pen color")
Tpwidth = input("Choose your pen width")
t.color(Tcolour)
t.pensize(Tpwidth)
Select = int(input("""________________________________________
Select Fractal variant:
0.Default
1.Fract1
2.Fract2
3.Fract3

________________________________________"""))

koch_(Select)(t,order,size)
