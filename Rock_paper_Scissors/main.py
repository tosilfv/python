from random import choice

num_rock_paper_or_scissors = ['0', '1', '2']
ascii_rock_paper_or_scissors = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
cpu_choice = choice(num_rock_paper_or_scissors)
if user_choice == '0':
    print(ascii_rock_paper_or_scissors[0])
    print('\nCPU CHOSE:\n')
    if cpu_choice == '0':
        print(ascii_rock_paper_or_scissors[0])
        print('\nTIE')
    elif cpu_choice == '1':
        print(ascii_rock_paper_or_scissors[1])
        print('\nCPU WINS')
    elif cpu_choice == '2':
        print(ascii_rock_paper_or_scissors[2])
        print('\nUSER WINS')
elif user_choice == '1':
    print(ascii_rock_paper_or_scissors[1])
    print('\nCPU CHOSE:\n')
    if cpu_choice == '1':
        print(ascii_rock_paper_or_scissors[1])
        print('\nTIE')
    elif cpu_choice == '2':
        print(ascii_rock_paper_or_scissors[2])
        print('\nCPU WINS')
    elif cpu_choice == '0':
        print(ascii_rock_paper_or_scissors[0])
        print('\nUSER WINS')
elif user_choice == '2':
    print(ascii_rock_paper_or_scissors[2])
    print('\nCPU CHOSE:\n')
    if cpu_choice == '2':
        print(ascii_rock_paper_or_scissors[2])
        print('\nTIE')
    elif cpu_choice == '0':
        print(ascii_rock_paper_or_scissors[0])
        print('\nCPU WINS')
    elif cpu_choice == '1':
        print(ascii_rock_paper_or_scissors[1])
        print('\nUSER WINS')
else:
    print('Game Over.')