import turtle
wn = turtle.Screen()
wn.bgpic("C:\\Users\\400T6B\\Desktop\\mymaze.gif")
t1 = turtle.Turtle()
def keyup():
    pt = t1.pos()
    print("up",pt)
    t1.write(pt)
    t1.forward(50)
def keyright():
    t1.rt(45)
def keyleft():
    t1.lt(45)
def keydown():
    t1.back(50)
def mousegoto(x, y):
    t1.goto(x,y)
def keydelete():
    t1.penup()
def keyappear():
    t1.pendown()

def isintrap(x, y, x1, y1, x2, y2):
    minx = min(x1, x2)
    maxx = max(x1, x2)
    miny = min(y1, y2)
    maxy = max(y1, y2)
    if x>=minx and x<=maxx and y>=miny and y<=maxy:
        return Ture
    return False

def drawRectWithFill(x1,y1,x2,y2,color):
    t1.goto(x1,y1)
    t1.fillcolor(color)
    t1.begin_fill()
    t1.goto(x2,y1)
    t1.goto(x2,y2)
    t1.goto(x1,y2)
    t1.goto(x1,y1)
    t1,end_fill()

def moveto(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()

def checkTrap(oldx, oldy):
    p =t1.pos()
    if isintrap(p[0], p[1], -200, -200, 200, 200):
        drawRectWithFill(-200, -200, 200, 200, "red")
        moveto(0, 0)

def mousegoto(x, y):
    moveto(x, y)

wn.onkey(keyup, "Up")
wn.onkey(keyright, "Right")
wn.onkey(keyleft, "Left")
wn.onkey(keydown, "Down")
wn.onkey(wn.bye, "q")
wn.onkey(keydelete, "s")
wn.onkey(keyappear, "a")
wn.onclick(mousegoto)
wn.listen()
turtle.mainloop()