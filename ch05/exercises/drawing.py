import turtle

def drawEqShape(myturtle=None, num_sides=0, side_length=0):
  num_sides = int(input("Enter the number of sides you want:"))
  side_length = int(input("Enter the side length you want:"))
  for i in range(num_sides):
    myturtle.forward(side_length)
    myturtle.left(360/num_sides)
  
leo = turtle.Turtle()
leo.color("blue")
drawEqShape(leo, 4, 10)