from random import randint

# play options
computerOptions = ["Rock", "Paper", "Scissors"]

# assign random play to computer
computer = computerOptions[randint(0, 2)]

playerFlag = False

while playerFlag != True:
  player = input("Rock, Paper or Scissors?")
  player = player.lower()
  player = player.capitalize()
  if player == "Rock" or player == "Paper" or player == "Scissors":
    playerFlag = True
  else:
    print("Retype your answer correctly")
    playerFlag == False
    
if player == computer:
  print("Tie!")
elif player == "Rock":
  if computer == "Paper":
    print("You lose! " + computer + " covers " + player)
  elif computer == "Scissors":
    print("You win! " + player + " breaks " + computer)
elif player == "Paper":
  if computer == "Scissors":
    print("You lose! " + computer + " cuts " + player)
  elif computer == "Rock":
    print("You win! " + player + " covers " + computer)
elif player == "Scissors":
  if computer == "Rock":
    print("You lose! " + computer + " breaks " + player)
  elif computer == "Paper":
    print("You win! " + player + " cuts " + computer)