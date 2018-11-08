import turtle



def koch(t, order, size):

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, angle2, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)
           



t = turtle.Turtle()
wn = turtle.Screen()
wn.title("Fractals")
order = int(input("Choose the Order: "))
size = int(input("""Choose the Size
|Be sure size is over 500!|: """)) #Dev note: Be sure to set the size >500
print ("________________________________________")
H = int(input("Choose your resolution height: "))
W =int(input("Choose your resolution width: "))
turtle.setup(H, W)
Tcolour = input("Choose your pen color: ")
Tpwidth = input("Choose your pen width: ")
t.color(Tcolour)
t.pensize(Tpwidth)
angle2 = int(input("""Enter angle2 
|IMPORTANT: SOME VALUES MAY CAUSE ODD RESULTS|: """)) #Be sure to set the angle to a negative, angles that work well are -60, -120, -180. Try and experiment with this!

koch(t,order,size)
