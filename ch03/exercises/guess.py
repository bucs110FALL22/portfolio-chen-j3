import random

answer = random.randrange(1,11)

for i in range(3):
  guess = int(input("Guess the number from 1-10."))
  if guess == answer:
    print("Correct!")
    elif guess > answer:
      print("Too high.")
    elif guess < answer:
      print("Too low.")