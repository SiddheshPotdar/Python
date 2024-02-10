import random

while True:
  choices = ['rock', 'paper', 'scissor']
  computer = random.choice(choices)
  # print(computer)

  player = None

  while player not in choices:
    player = input("rock, paper, scissor? : ").lower()

  # print(player)

  if player == computer:
    print("player: ",player)
    print("computer: ",computer)
    print("Tie!")
  elif player == 'rock':
    if computer == 'paper':
      print("player: ",player)
      print("computer: ",computer)
      print("You lost!")
    elif computer == 'scissor':
      print("player: ",player)
      print("computer: ",computer)
      print("You won!")
  elif player == 'paper':
    if computer == 'scissor':
      print("player: ",player)
      print("computer: ",computer)
      print("You lost!")
    elif computer == 'rock':
      print("player: ",player)
      print("computer: ",computer)
      print("You won!")
  else:
    if computer == 'paper':
      print("player: ",player)
      print("computer: ",computer)
      print("You won!")
    elif computer == 'rock':
      print("player: ",player)
      print("computer: ",computer)
      print("You lost!")

  play_again = input("do you want to play again? (y/n): ").lower()
  if play_again != "y":
    break

print("Bye!")
