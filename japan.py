import turtle as t

def write_xy(x,y):
    t.goto(x,y)
    t.stamp()
    t.write("x:%d, y:%d"%(x,y))

def screen_clear(x,y):
      t.goto(x,y)
      t.clear()

t.setup(600,600)
t.shape("circle")
s=t.Screen()
t.penup()
s.onscreenclick(write_xy,1)
s.onscreenclick(scrren_cleer,3)
s.listen()
