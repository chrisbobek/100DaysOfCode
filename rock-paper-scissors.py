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
'''
         SYSTEM
       R   P   S
 P   |---|---|---|
 L R | T | P | R | 
 A   |---|---|---|
 Y P | P | T | S | 
 E   |---|---|---|
 R S | R | S | T | 
     |---|---|---|  
'''

options = [rock, paper, scissors]

rock_row = ['Tie!\n', 'Paper beats rock! Player loses.\n', 'Rock beats scissors! Player loses.\n']
paper_row = ['Paper beats rock! Player wins!\n', 'Tie!\n', 'Scissors beats paper! Player loses.\n'] 
scissors_row = ['Rock beats scissors! Player loses.\n', 'Scissors beat paper! Player wins!\n', 'Tie!\n'] 
   
grid = [rock_row, paper_row, scissors_row]

instructions = "\nType 0 to throw down a rock, 1 to throw down paper, or 2 to throw down scissors.\nGo!\n"
player = input(instructions)
player = int(player)
print("\nYou chose:")
print(options[player])

system = random.randint(0,2)
print("\nThe system chose:")
print(options[system])

print(grid[player][system])

