import pygame
import random
import math

#setup
pygame.init()
screen = pygame.display.set_mode((500,500))
size = pygame.display.get_window_size()
width = size[0]
height = size[1]

#choose player
pygame.draw.rect(screen, "purple", (0,0,width/2,height))
pygame.draw.rect(screen, "green", (width/2,0,width/2,height))
pygame.display.update()
purpleScore = 0
greenScore = 0
playerSelect = ""
print("Click on the the purple or green to guess which color will win.")
guess = True
while guess:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.pos[0] < width/2:
        playerSelect = "purple"
        guess = False
      elif event.pos[0] > width/2:
        playerSelect = "green"
        guess = False
print("Let's see if player" , playerSelect, "will win.")
pygame.time.wait(1000)

#dart board
screen.fill((191,227,255))
pygame.draw.circle(screen,"lightpink", (width/2,height/2), 250)
pygame.draw.line(screen,"black", (width/2,0), (height/2,height), width=2)
pygame.draw.line(screen, "black", (0,height/2), (width, width/2), width=2)
pygame.display.update()

#throw darts
for i in range(10):
  purple_x1 = random.randrange(0,width+1)
  purple_y1 = random.randrange(0,height+1)
#determine if dart lands inside circle
  distance_from_center = math.hypot(purple_x1 - (width/2), purple_y1 - (height/2))
  is_in_circle = distance_from_center <= width/2
  if is_in_circle == True:
    pygame.draw.circle(screen, "purple", (purple_x1, purple_y1), 5)
    purpleScore += 1
  else:
    pygame.draw.circle(screen, "black", (purple_x1, purple_y1), 5)
  green_x1 = random.randrange(0,width+1)
  green_y1 = random.randrange(0,height+1)
  distance_from_center = math.hypot(green_x1 - (width/2), green_y1 - (height/2))
  is_in_circle = distance_from_center <= width/2
  if is_in_circle == True:
    pygame.draw.circle(screen, "green", (green_x1, green_y1), 5)
    greenScore += 1
  else:
    pygame.draw.circle(screen, "gray", (green_x1, green_y1), 5)
  pygame.display.update()
  print("The score for purple is", purpleScore, ". The score for green is", greenScore)
  pygame.time.wait(2000)
#update score

if purpleScore > greenScore and playerSelect == "purple":
  print("You are correct. Purple won.")
elif purpleScore > greenScore and playerSelect == "green":
  print("Unlucky guess. Purple won.")
elif purpleScore < greenScore and playerSelect == "green":
  print("You are correct. Green won.")
elif purpleScore < greenScore and playerSelect == "purple":
  print("Unlucky guess. Green won.")
else:
  print("It was a tie!")