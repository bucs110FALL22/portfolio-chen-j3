import turtle

window = turtle.Screen()
window.setup(500,500)
window.bgcolor("white")
duolingo = turtle.Turtle()

#introduction
def lang():
  language = input("Input what language you would like to learn out of these options: French, Spanish, Chinese \n")
  language = language.lower()
  if language == "french":
    return "Bonjour"
  elif language == "chinese":
    return "Ni Hao"
  elif language == "spanish":
    return "Hola"
  else:
    return "The system does not include that language yet"

#inspired by the Duolingo app
def appShape():
  duolingo.color("gold", "#7ac70c")
  duolingo.begin_fill()
  for i in range(4):
    duolingo.forward(250)
    duolingo.left(90)
  duolingo.end_fill()

#function for position after noticing a repetition of duolingo.up duolingo.goto duolingo.down and duolingo.begin_fill()
def pos(x=0, y=0):
  duolingo.up()
  duolingo.goto(x,y)
  duolingo.down()
  duolingo.begin_fill()
  
#function for all ovals in Duo's eyes and mouth
def oval(radius):
  for i in range(2):
    duolingo.circle(radius,90)
    duolingo.circle(radius//2,90)

#function for the white part of Duo's eyes
def duoScelera():
  duolingo.color("#8ee000", "white")
  duolingo.seth(-135)
  oval(60)
  duolingo.end_fill()

#function for the black part of Duo's eyes
def duoPupils():
  duolingo.color("black")
  duolingo.seth(-135)
  oval(33)
  duolingo.end_fill()

#function for the white part in the black part of Duo's eyes
def duoSparkles():
  duolingo.color("white")
  pos(-72,5)
  duolingo.seth(20)
  oval(12)
  duolingo.end_fill()
  pos(46,5)
  duolingo.seth(20)
  oval(12)
  duolingo.end_fill()

#combines all the functions to create the full image of both of Duo's eyes so the main code is shorter and easier to read
def duoEyes():
  # duolingo.color("#8ee000")
  # pos(0,0)
  
  pos(-85,40)
  duoScelera()
  pos(45,40)
  duoScelera()
  pos(-70,20)
  duoPupils()
  pos(50,20)
  duoPupils()
  duoSparkles()

def duoMouth():
  duolingo.color("#faa918")
  duolingo.seth(-90)
  duolingo.circle(20,180)
  duolingo.end_fill()
  
def duoBeak():
  duolingo.color("#ffc715")
  pos(33,-50)
  duolingo.begin_fill()
  duolingo.seth(90)
  duolingo.circle(31,180)
  duolingo.end_fill()
  duolingo.color("#F1D888")
  pos(11,-25)
  duolingo.seth(135)
  oval(12)
  duolingo.end_fill()

#drivers code
def main():
  duolingo.screen.title("Duolingo App")
  duolingo.shape("arrow")
  print("Duolingo is a language learning app.")
  print(lang())
  pos(-125,-125)
  appShape()
  duoEyes()
  pos(-17.5,-50)
  duoMouth()
  duoBeak()
  duolingo.up()
  duolingo.goto(-250,250)
main()


window.exitonclick()