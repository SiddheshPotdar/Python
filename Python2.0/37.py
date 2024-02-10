#  Quiz game

questions = {
  "Who created Python?: " : 'A',
  "What year was Python created?: " : 'B',
  "Python is tributed to which comedey group?: " : 'C',
  "Is the Earth round?: " : 'A' 
}

options = [
  ['A. Guido vann Rossum', 'B. Elon Musk', 'C. Mask Zuckerberg', 'D. Bill Gates'], 
  ['A. 1989', 'B. 1991', 'C. 1990', 'D. 2003'],
  ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'], 
  ['A. True', 'B. False', 'C. sometimes', 'D. What is Earth?',]
]

# ----------------------------------------------------------------

def  new_game():
  
  guesses = []
  correct_guesses = 0
  question_num = 0

  for key in questions:
    print("--------------------")
    print(key)

    for i in options[question_num]:
      print(i)

    guess = input("Enter you answer (A/B/C/D):").upper()
    guesses.append(guess)

    correct_guesses += check_answer(guess, questions.get(key))

    question_num += 1

  display_score(correct_guesses)

  play_again()

# ---------------------------------------------------------------

def check_answer(guess, answer):
  if guess == answer:
    print("Correct Answer")
    return 1
  else:
    print("Wrong Answer")
    return 0


# ---------------------------------------------------------------

def display_score(correct_guesses):
  score = (correct_guesses / len(questions))*100
  print("Your score is {}%.".format(int(score)))

  
  

# ---------------------------------------------------------------

def play_again():
  again = input("Do you want to play again? (y/n): ").lower()
  if again == "y":
    new_game()

# ---------------------------------------------------------------

new_game()