import turtle
#create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()
#hide the cursor
babbage.hideturtle()
#draw stem and turtle
babbage.color("green","black")
babbage.left(90)
babbage.forward(100)
babbage.right(90)
#draw center
babbage.color("black","black")
babbage.begin_fill()
babbage.circle(10)
babbage.end_fill()
#draw 24 petals
for i in range(1,24):
    babbage.left(15)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
#tidy up window
window.exitonclick()
