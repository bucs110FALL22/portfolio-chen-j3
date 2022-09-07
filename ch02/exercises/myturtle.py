import turtle

my_turtle = turtle.Turtle() #Factories

window = turtle.Screen()
window.bgcolor("white")
#window.exitonclick()

my_turtle.shape("turtle")
my_turtle.color("purple")
#create 50x50 square
my_turtle.left(0)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
#differnt location
my_turtle.up()
my_turtle.forward(20)
my_turtle.down()
#second square
my_turtle.color("red")
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)

window.exitonclick()