import turtle as t
t.speed(1)
t.penup()
t.setpos(-100,100)
t.pendown()
t.pencolor(0.8,0.4,0.2)
t.pensize(3)
for i in range(3):
    t.forward(300)
    t.right(120)
t.penup()
t.forward(100)
t.left(60)
t.forward(100)
t.pendown()
for i in range(3):
    t.right(120)
    t.forward(300)
t.exitonclick()