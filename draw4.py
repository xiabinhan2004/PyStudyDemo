import turtle as t
t.penup()
t.goto(-200,200)
t.pendown()
t.pensize(2)
t.speed(1)
b = eval(input("side"))
c=input("color")

t.color("blue",c)
t.begin_fill()
for i in  range(b):
    t.forward(200)
    t.right(360/b)
t.end_fill()
t.exitonclick()