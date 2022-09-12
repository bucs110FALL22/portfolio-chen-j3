import turtle

slay = turtle.Turtle() #Factories

window = turtle.Screen()
window.bgcolor("white")
slay.shape("turtle")
sides = int(input("Enter the number of sides your shape has. \n"))
length = int(input("Enter the length of the sides. \n"))
color = input("What color do you want your turtle to be? \n")
slay.color(color)

for i in [0]*sides:
  slay.left(360/sides)
  slay.forward(length)

window.exitonclick()