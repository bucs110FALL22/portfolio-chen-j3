import pygame
pygame.init()

#part A 
n = 101
while n != 1:
  if n%2 == 0:
    n = n//2
  elif n%2 != 0:
    n = n*3 + 1
  print("The sequence includes", n)
  
#part B 
upper_limit = 20
iters = {}
for start in range(2,upper_limit+1):
  count = 0
  n = start
  while n != 1:
    if n%2 == 0:
      n = n//2
    elif n%2 != 0:
      n = n*3 + 1
    count = count + 1
    print("The count value is", count)
    print("The sequence is", n)
    iters[start] = count
    #dictionaries always create key value pairs
print(iters)

#part C 
screen = pygame.display.set_mode()
screen.fill("white")
font = pygame.font.Font("arial.ttf",20)
upper_limit = int(input("Enter an integer for the upper limit "))
iters = {}
max_so_far = 0
max_val = 0
scale = 5 #use as multiplier so when generate x and y coordinates graph is not tiny
for i in range(2,upper_limit+1):
  pygame.display.flip()
  count = 0
  n = i
  while n != 1:
    if n%2 == 0:
      n = n//2
    elif n%2 != 0:
      n = n*3 + 1
    count = count + 1
    iters[i] = count
    iters.items() #save list of coordinates
    coordinates = list(iters.items())
  pygame.draw.lines(screen, "red", False, coordinates) #pass the coordinates
  #you will need to ensure you have at least 2 coordinates in the list to draw the graph, which means you will need to wrap this in an if statement checking the length of your coordinates list
  pygame.display.flip()
  #if the max so far is less than the count update max_so_far and max_val
  if max_so_far < count:
    max_so_far = count
    max_val = count
  #create message string
  msg = font.render(str(max_so_far), True, "black")
  screen.blit(msg,(10,10))
  #render message
  #blit maximum message onto display
  pygame.display.flip()
