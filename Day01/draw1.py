import turtle as t
t.penup()
t.goto(-100,100)
t.pendown()
num=200
while(t.xcor()!=0 and t.ycor()!=0):
    # t.forward(num)
    # t.right(90)
    # t.forward(num)
    # t.right(90)
    # num *= 0.9
    # t.forward(num)
    # t.right(90)
    # num*=0.9
    # t.forward(num)
    # t.right(90)
    num*=0.95
    t.forward(num)
    t.right(90)
    print(t.pos())
t.exitonclick()
