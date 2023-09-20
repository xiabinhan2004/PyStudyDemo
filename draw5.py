import math
import turtle as t
t.pencolor("blue")
for i in range(3):
    t.forward(100)
    t.right(120)
    print(t.pos())
t.penup()
t.goto(-50,-50*math.sqrt(3))
t.pendown()
t.pencolor("red")
for i in range(3):
    t.forward(200)
    t.left(120)
    print(t.pos())
t.exitonclick()