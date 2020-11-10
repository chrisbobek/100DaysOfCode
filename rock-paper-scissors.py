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

options = [rock, paper, scissors]

instructions = "\nType 0 for rock, 1 for paper, or 2 for scissors. Go!\n"
player = input(instructions)
player = int(player)

print("You chose:\n")
print(options[player])

system = random.randint(0,2)
print("\nThe system chose:\n")
print(options[system])



