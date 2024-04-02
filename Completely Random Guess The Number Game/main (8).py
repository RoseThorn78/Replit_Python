import random
counter = 1
print("Competely Random Guess the Number Game!")
print()
print("Guess a number between 1 and 1,000,000 - see how many attempts it takes you!!")
number = random.randint(1,1000000)
for  i in range(1,1000000):
  guess = int(input("Make your guess: "))
  print()
  if guess > number:
    print("AHHHH, TOO HIGH!!!")
    print("Try again")
    counter += 1
    continue
  elif guess == number: 
    print("DING, DING, DING!")
    print("WE HAVE A WINNER!!!!🤩🥳 CONGRATULATIONS!!!")
    print("It only took you",counter,"attempt(s)!")
    print()
    print("Click 'run' to try again with a different number.")
    exit()
  else:
    if guess >= 1:
      print("Oops, that's a bit too low...")
      print("Try again")
      counter += 1
      continue
    else:
      print("Uh,oh! You guessed a negative number!")
      print("This means you failed... 😢")
      exit()
