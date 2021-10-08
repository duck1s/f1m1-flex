import turtle
def squares(length, colour):
  turtle.pencolor(colour)
  turtle.pensize(4)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.setheading(360)
  turtle.ht()
for number in range(50,110,10):
  squares(number,"red")