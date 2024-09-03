import random

choices = {
    "Rock":'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''',
"Paper":'''
     ______
---'   ____)_____
          _______)
          _________)
         _________)
---.____________)''',
"Scissors":'''
    _______
---'   ____)_____
          _______)
       ____________)
      (____)
---.__(___)'''
}

choices_list = [key for key,value in choices.items()]

vs = '''

              $$\         
             $$  |        
$$\    $$\  $$  /$$$$$$$\ 
\$$\  $$  |$$  /$$  _____|
 \$$\$$  /$$  / \$$$$$$\  
  \$$$  /$$  /   \____$$\ 
   \$  /$$  /   $$$$$$$  |
    \_/ \__/    \_______/ '''

print("WELCOME TO THE GAME 0F ROCK, PAPER AND SCISSORS")
print("You will get 2 points for Win, 1 point for Tie and no point for Lose.")
print("Let's Play!")

play =True
user_score = 0
comp_score = 0

while play:
    user_input = input("Choose your weapon (Rock,Paper,Scissors): ").title()
    comp_input = random.choice(choices_list)
    print(f"The computer chose {comp_input}")
    print(f"{choices[user_input]} {vs} {choices[comp_input]}\n")
    if user_input == comp_input:
        print("Tie!")
        user_score += 1
        comp_score += 1
    elif (choices_list.index(user_input) + 1 ) % (len(choices_list)) == choices_list.index(comp_input):
        print("You Lose!")
        comp_score += 2
    else:
        print("You Win!")
        user_score += 2
    print(f"The score are as follows: YOU -> {user_score} , COMPUTER -> {comp_score}")
    play_again = input("Do you want to play again (y/n):").lower()
    if play_again == "n":
        play = False