import random

num = random.randrange(1,11)
num_guesses = 0 #to keep track of number of guesses

for i in range(3):
  guess_num = int(input("Please enter a guess:"))
  #num_guesses = num_guesses + 1
  num_guesses +=1
  if guess_num > num:
      print("your guess is too high")
  elif guess_num < num:
      print("your guess is too low")
  else:
    print("Correct!")
  break
  
print("It took you", num_guesses, "to get it right.")

# import random

# answer = random.randrange(1,11) #gives one number between the range

# for i in range(3): #use range to create list . list of 3 things - loop 3 times
#   #i is a variable name 
#   guess = int(input("Guess the number from 1-10."))
#   if guess == answer:
#     print("Correct!")
#     elif guess > answer:
#       print("Too high.")
#     else:
#       print("Too low.")

#       break
# print ("It took you" num_guesses, "to guess the correct number.")


# #to end loop - flag variable approach
# # correct_guess = False (before i in range line)

# #other approach - break