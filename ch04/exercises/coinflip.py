# import turtle
# import random

# window = turtle.Screen()
# turtle = turtle.Turtle()
# # turtle begins center of screen
# turtle.goto(0,0)

# #flip a coin
# coin = random.randrange(0,2)
# if coin == 0:
#     #coin is head
# else: #coin == 1:
#     #coin is tails

# #calculate if turtle is on screen

# window.exitonclick()


import random
import turtle


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')

t.speed(0) #makes it faster

#make a function for if turtle is off screen bc will be used a lot
# def isinscreen(window, turt):
#   turtleX = t.xcor()
#     turtleY = t.ycor()

#     x_range = wn.window_width()/2 #
#     y_range = wn.window_height()/2
#     if abs(turtleX) > x_range or abs(turtleY) > y_range: 
#       return False
#   return True


distance = 10
angle = 90
is_in_screen = True

colors = ["green", "blue", "purple"]

while is_in_screen: # we can worry about this later, and just make a dummy function
    coin = random.randrange(0, 2) #create 50% - use 0 and 1
    if coin == 0:           # heads
        t.left(angle)
    else:                      # tails
        t.right(angle)
    t.forward(distance)
    # t.forward(16) #magic number.data
    turtleX = t.xcor()
    turtleY = t.ycor()

    x_range = wn.window_width()/2 #bc the center for turtle is at 0,0
    y_range = wn.window_height()/2
    
    t.color(colors[0]) #j to make it pretty
    colors.append(colors.pop(0))
    if abs(turtleX) > x_range or abs(turtleY) > y_range: 
      #if greater thann range, then it is out of the screen
        is_in_screen = False
        
wn.bgcolor("yellow")
wn.exitonclick()

