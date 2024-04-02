#stops either player from viewing each others input
from getpass import getpass as input

#collects scores for player 1 and 2
score1 = 0
score2 = 0
  
print("ULTIMATE ROCK🪨, PAPER📄, SCISSORS✂️ !")
print()
  
print("Let the game begin!")
print("Good luck players!")
print()
  
#loop to repeat the game
while True:

#players choose moves
  p1 = input("Player 1, please select your move(R, P or S): ")
  p2 = input("Player 2,please select your move(R, P or S): ")
  print()

  #converts user input (R,S,P) into "Rock", "Paper", "Scissors"
  if p1 == "R" or p1 == "r":
    p1Result = "ROCK🪨"
  elif p1 == "P" or p1 == "p":
    p1Result = "PAPER📄"
  elif p1 == "S" or p1 == "s":
    p1Result = "SCISSORS✂️"
  else:
    print("Try again") 
  if p2 == "R" or p2 == "r":
    p2Result = "ROCK🪨"
  elif p2 == "P" or p2 == "p":
    p2Result = "PAPER📄"
  elif p2 == "S" or p2 == "s":
    p2Result = "SCISSORS✂️"
  else:
    print("Try again")
  
  #collects data on which player won each round
  if p1Result == "ROCK🪨" and p2Result == "ROCK🪨":
    print("Both Player 1 and Player 2 picked ROCK🪨!")
    print("It was a tie!")
    results = "TIE"
  elif p1Result == "ROCK🪨" and p2Result == "SCISSORS✂️":
    print("Player 1's ROCK🪨 completely obliterated Player 2's SCISSORS✂️!")
    print("Player 1 WINS!!!")
    results = "P1"
  elif p1Result == "ROCK🪨" and p2Result == "PAPER📄":
    print("Yeesh! Player 1's ROCK🪨 was smothered by Player 2's PAPER📄!")
    print("Player 2 WINS!!!")
    results = "P2"
  elif p1Result == "SCISSORS✂️" and p2Result == "ROCK🪨":
    print("Player 2's ROCK🪨 completely obliterated Player 1's SCISSORS✂️!")
    print("Player 2 WINS!!!") 
    results = "P2"
  elif p1Result == "PAPER📄" and p2Result == "ROCK🪨":
    print("Yeesh! Player 2's ROCK🪨 was smothered by Player 1's PAPER📄!")
    print("Player 1 WINS!!!") 
    results = "P1"
  elif p1Result == "PAPER📄" and p2Result == "PAPER📄":
    print("Both Player 1 and Player 2 picked PAPER📄!") 
    print("It was a tie!")
    results = "tie"
  elif p1Result == "PAPER📄" and p2Result == "SCISSORS✂️":
    print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
    print("Player 2 WINS!!!")
    results = "P2"
  elif p1Result == "SCISSORS✂️" and p2Result == "PAPER📄":
    print("Wow, Player 2's SCISSORS✂️ absolutely shredded Player 1's PAPER📄!")
    print("Player 1 WINS!!!")
    results = "P1"
  else:
    print("Both Player 1 and Player 2 picked SCISSORS✂️!") 
    print("It was a tie!")
    results = "tie"
    
  #score results
  if results == "P1":
    score1 += 1
  elif results == "P2":
    score2 += 1
  else: 
    score1 += 0
    score2 += 0

  #final results
  if score1 == 3:
    print()
    print("Congratulations, Player 1! You've won this game of ULTIMATE ROCK🪨, PAPER📄, SCISSORS✂️!")
    exit()
  elif score2 == 3:
    print()
    print("Congratulations, Player 2! You've won this game of","\033[36m","ULTIMATE ROCK🪨, PAPER📄, SCISSORS✂️!","\033[0m")   
    exit()
  else:
    print()
    continue
