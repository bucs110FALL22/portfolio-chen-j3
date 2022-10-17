def percentage_to_letter(score=0):
  if score >= 90:
    return "A"
  elif score < 90 and score >= 80:
    return "B"
  elif score < 80 and score >= 70:
    return "C"
  elif score < 70 and score >= 60:
    return "D"
  elif score < 60:
    return "F"

def is_passing(letter=None):
  if letter == "A" or letter == "B" or letter == "C":
    return True
  else:
    return False
    
#driver code
score = float(input("What is your score? "))
letter = percentage_to_letter(score)
print("Your grade letter is", letter)
print("You are passing." ,is_passing(letter))