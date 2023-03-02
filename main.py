print("\033[34m", "Welcome to your adventure story simulator!", "\033[37m")
print(
    "First, I am going to ask you some questions to personalise this story for you."
)
print()
print("\033[32m")
userName = input("What is your name?: ")
print("\033[31m")
worstEnemy = input("Who is your worst enemy?: ")
print("\033[33m")
favouriteFood = input("What is your favourite food?: ")
print("\033[35m")
superPower = input("What is your super power?: ")
print("\033[36m")
bestFriend = input("What is your best friend's name?: ")
print("\033[37m")
print()
print("It is a beautiful, sunny morning. Our hero,", "\033[32m", userName,
      "\033[37m", ",is at home with their bestfriend,", "\033[36m", bestFriend,
      "\033[37m", " ,eating", "\033[33m", favouriteFood, "\033[37m", ".")
print("Just then,", "\033[31m", worstEnemy, "\033[37m", "shows up.")
print("'Why can't you just leave us alone,", "\033[31m", worstEnemy, "'",
      "\033[36m", bestFriend, "\033[37m", "grumbles.")
print("'Don't worry,", "\033[36m", bestFriend, "\033[37m", "'", "\033[32m",
      userName, "\033[37m", "replies.", "\033[31m", worstEnemy, "\033[37m",
      "must have forgotten that", "\033[32", "our hero has the power of",
      "\033[35m", superPower, "\033[37m", "!")
print("Bammm! After a short, 5 minute battle,", "\033[31m", worstEnemy,
      "\033[37m", "has been defeated!")
print("Finally,", "\033[32m", userName, "\033[37m", "and", "\033[36m",
      bestFriend, "\033[37m", "can go back to eating their", "\033[33m",
      favouriteFood, "\033[37m", ".")
print("\033[34m", "THE END")
