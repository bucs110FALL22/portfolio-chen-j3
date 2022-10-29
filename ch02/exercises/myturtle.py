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

#prof solution
# import turtle

# CIRCLE_DEG = 360

# wn = turtle.Screen()

# michelangelo = turtle.Turtle()
# michelangelo.shape('turtle')

# sides = 4  #no magic numbers
# length = 50
# #list of colors that the turtle will use

# michelangelo.color("purple")
# #move the turtle forward by length
# michelangelo.forward(length)
# # caluclate the angle of the turn,
# # and change the turtle heading
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)

# michelangelo.up()
# michelangelo.forward(100)
# michelangelo.down()

# michelangelo.color("red")

# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)
# michelangelo.forward(length)
# michelangelo.left(CIRCLE_DEG / sides)

# wn.exitonclick()