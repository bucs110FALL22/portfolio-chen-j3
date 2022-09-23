import turtle #1. import modules
import random
import pygame
import math

# #Part A
# window = turtle.Screen() # 2.  Create a screen
# window.bgcolor('lightblue')

# michelangelo = turtle.Turtle() # 3.  Create two turtles
# leonardo = turtle.Turtle()
# michelangelo.color('orange')
# leonardo.color('blue')
# michelangelo.shape('turtle')
# leonardo.shape('turtle')
# michelangelo.up() # 4. Pick up the pen so we don’t get lines
# leonardo.up()
# michelangelo.goto(-100,20)
# leonardo.goto(-100,-20)
# #own code to change the speed of turtles
# leonardo.speed(1)
# michelangelo.speed(1)

# ## 5. Your PART A code goes here
# # part A pt 1
# distance = random.randrange(1,101)
# leonardo.forward(distance)
# michelangelo.forward(distance)
# leonardo.goto(-100,20)
# michelangelo.goto(-100,-20)

# # part A pt 2
# for i in range(10):
#   distanceTwo = random.randrange(0,11)
#   leonardo.forward(distanceTwo)
#   michelangelo.forward(distanceTwo)
  
# leonardo.goto(-100,20)
# michelangelo.goto(-100,-20)


# PART B - complete part B here
#equilateral triangle
#1
pygame.init()
window = pygame.display.set_mode()
window.fill("white")

coords = []
num_sides = 3
side_length = 50
offset = 100
#2
for i in range(num_sides):
  theta = (2.0 * math.pi * i/num_sides)
  print("The theta for each side of the polygon is", theta)
  x = side_length * math.cos(theta) + offset
  print("The x coordinate is", x)
  y = side_length * math.sin(theta) + offset
  coords.append([x,y]) #add each coord to the list of coords

print("The coordinates of this polygon are", coords)
#3
pygame.draw.polygon(window,"blue", (coords))
#4
pygame.display.flip()
#5
pygame.time.wait(1000)
#6
window.fill("white")
pygame.display.flip()

#square
coords = []
num_sides = 4
for i in range(num_sides):
  theta = (2.0 * math.pi * i/num_sides)
  print("The theta for each side of the polygon is", theta)
  x = side_length * math.cos(theta) + offset
  print("The x coordinate is", x)
  y = side_length * math.sin(theta) + offset
  coords.append([x,y]) 
print("The coordinates of this polygon are", coords)
pygame.draw.polygon(window,"blue", (coords))
pygame.display.flip()
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip()

#hexagon
coords = []
num_sides = 6
for i in range(num_sides):
  theta = (2.0 * math.pi * i/num_sides)
  print("The theta for each side of the polygon is", theta)
  x = side_length * math.cos(theta) + offset
  print("The x coordinate is", x)
  y = side_length * math.sin(theta) + offset
  coords.append([x,y]) 
print("The coordinates of this polygon are", coords)
pygame.draw.polygon(window,"blue", (coords))
pygame.display.flip()
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip()

#nonagon
coords = []
num_sides = 9
for i in range(num_sides):
  theta = (2.0 * math.pi * i/num_sides)
  print("The theta for each side of the polygon is", theta)
  x = side_length * math.cos(theta) + offset
  print("The x coordinate is", x)
  y = side_length * math.sin(theta) + offset
  coords.append([x,y]) 
print("The coordinates of this polygon are", coords)
pygame.draw.polygon(window,"blue", (coords))
pygame.display.flip()
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip()

#circle
coords = []
num_sides = 360
for i in range(num_sides):
  theta = (2.0 * math.pi * i/num_sides)
  print("The theta for each side of the polygon is", theta)
  x = side_length * math.cos(theta) + offset
  print("The x coordinate is", x)
  y = side_length * math.sin(theta) + offset
  coords.append([x,y]) 
print("The coordinates of this polygon are", coords)
pygame.draw.polygon(window,"blue", (coords))
pygame.display.flip()
pygame.time.wait(1000)
window.fill("white")
pygame.display.flip()

#window.exitonclick()
