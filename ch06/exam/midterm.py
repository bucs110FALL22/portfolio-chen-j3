import turtle

YELLOWORANGE = "#faa918"

#introduction
def lang():
  ''' 
  This function does not draw anything. It asks the user what language they would like to learn.
  return: (string) Something in the language that was inputted.
  '''
  language = input("Input what language you would like to learn out of these options: French, Spanish, Chinese \n")
  language = language.lower()
  if language == "french":
    return "Bonjour le monde. (Hello world.)"
  elif language == "chinese":
    return "你好世界. (Hello world.)"
  elif language == "spanish":
    return "Hola Mundo. (Hello world.)"
  else:
    return "The system does not include that language yet."

#inspired by the Duolingo app
def appShape(duolingo):
  '''
  This function draws a square.
  '''
  duolingo.color("gold", "#7ac70c")
  duolingo.begin_fill()
  for i in range(4):
    duolingo.forward(250)
    duolingo.left(90)
  duolingo.end_fill()

#function for position after noticing a repetition of duolingo.up duolingo.goto duolingo.down and duolingo.begin_fill()
def pos(duolingo, x=0, y=0):
  '''
  Sets the position and gets ready to draw the next feature of Duo without drawing a line.
  x: (int) horizontal coordinate
  y: (int) vertical coordinate
  return: (string) both x and y coordinates
  '''
  duolingo.up()
  duolingo.goto(x,y)
  duolingo.down()
  duolingo.begin_fill()
  return "(x,y)"
  
#function for all ovals in Duo's eyes and mouth
def oval(duolingo, radius=5):
  '''
  This function creates ovals that are used in Duolingo's features.
  radius: (integer) the radius of the circles used to create ovals
  '''
  for i in range(2):
    duolingo.circle(radius,90)
    duolingo.circle(radius//2,90)

#function for the white part of Duo's eyes
def duoScelera(duolingo):
  '''
  This function creates uses the oval function, where the integer argument radius is set to 60, to create the scelera part of Duo's eyes.
  radius: (integer) the radius of the circles used to create ovals
  '''
  duolingo.color("#8ee000", "white")
  duolingo.seth(-135)
  oval(duolingo, 60)
  duolingo.end_fill()

#function for the black part of Duo's eyes
def duoPupils(duolingo):
  '''
  This function creates uses the oval function, where the integer argument radius is set to 33, to create the pupils of Duo's eyes.
  '''
  duolingo.color("black")
  duolingo.seth(-135)
  oval(duolingo, 33)
  duolingo.end_fill()

#function for the white part in the black part of Duo's eyes
def duoSparkles(duolingo):
  '''
  This function creates uses the oval function, where the integer argument radius is set to 12, to create the white part that is in the black part of Duo's eyes.
  '''
  duolingo.color("white")
  pos(duolingo, -72,5)
  duolingo.seth(20)
  oval(duolingo, 12)
  duolingo.end_fill()
  pos(duolingo, 46,5)
  duolingo.seth(20)
  oval(duolingo, 12)
  duolingo.end_fill()

#combines all the functions to create the full image of both of Duo's eyes so the main code is shorter and easier to read
def duoEyes(duolingo):
  '''
  This function combines the pos function that used integer arguments to create the coordinates, and the functions for each part of Duo's eyes, which also used oval functions in order to complete the full image of both eyes.
  '''
  pos(duolingo, -85,40)
  duoScelera(duolingo)
  pos(duolingo, 45,40)
  duoScelera(duolingo)
  pos(duolingo, -70,20)
  duoPupils(duolingo)
  pos(duolingo, 50,20)
  duoPupils(duolingo)
  duoSparkles(duolingo)

def duoMouth(duolingo):
  '''
  This function creates Duo's mouth.
  '''
  duolingo.color()
  duolingo.seth(-90)
  duolingo.circle(20,180)
  duolingo.end_fill()
  
def duoBeak(duoturtle=None):
  '''
  This function creates Duo's beak by using the pos function, which uses the integer arguments to create the position, and the oval function, which uses integer arguments for the radius used to create the oval shape.
  '''
  duoturtle.color("#ffc715")
  pos(duoturtle, 33,-50)
  duoturtle.begin_fill(YELLOWORANGE)
  duoturtle.seth(90)
  duoturtle.circle(31,180)
  duoturtle.end_fill()
  duoturtle.color("#F1D888")
  pos(duoturtle, 11,-25)
  duoturtle.seth(135)
  oval(duoturtle, 12)
  duoturtle.end_fill()

#drivers code
def main():
  window = turtle.Screen()
  window.setup(500,500)
  window.bgcolor("#C8EBF8")
  duolingo = turtle.Turtle()
  duolingo.speed(0)
  duolingo.screen.title("Duolingo App")
  duolingo.shape("arrow")
  print("Duolingo is a language learning app.")
  print(lang())
  pos(duolingo, -125,-125)
  appShape(duolingo)
  duoEyes(duolingo)
  pos(duolingo, -17.5,-50)
  duoMouth(duolingo)
  duoBeak(duolingo)
  duolingo.up()
  duolingo.goto(-250,250)
  window.exitonclick()
main()


