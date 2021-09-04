import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
choice = int((input("What do you choose? 0 for rock, 1 for paper, 2 for scissors")))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer's choice :")
c_choice = random.randint(0, 2)
print(game[c_choice])

if c_choice > choice:
    print(c_choice)
    print("Computer Wins!!")
elif choice > c_choice:
    print(choice)
    print("You Win!!")
elif choice == c_choice:
    print("Draw")
else:
    print("Invalid number!")