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

#Write your code below this line 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

choose = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
opponent = random.randint(0, 2)
images = [rock, paper, scissors]
print(images[choose])
print("Computer chose:")
print(images[opponent])
if choose == opponent:
  print("Draw")
elif choose == 0 and opponent == 2:
  print("You win!")
elif choose == 1 and opponent == 0:
  print("You win!")
elif choose == 2 and opponent == 1:
  print("You win!")
else:
  print("You lose!")
