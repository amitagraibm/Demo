import random
rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computerSelection =['rock','paper','scissors']
Player1Selection = input('Please make a choice of rock, paper and scissors" \n').lower()
def sel( palyer1, player2):
  winner = ''
  if palyer1 == 'rock' and player2 == 'scissors':
    winner = 'You'
  elif palyer1 == 'rock' and player2 == 'paper':
    winner = 'Computer'
  elif palyer1 == 'paper' and player2 == 'rock':
    winner ='You'
  elif palyer1 == 'paper' and player2 == 'scissors':
    winner ='Computer'
  elif palyer1 == 'scissors' and player2 == 'paper':
    winner ='You'
  elif palyer1 == 'scissors' and player2 == 'rock':
    winner ='Computer'
  else:
    winner ='Draw'
  return winner

if Player1Selection =="rock":
  print("Your choice is :" )
  print(rock)
  #computerChoice=""
  computerChoice = random.choice(computerSelection)
  print(computerChoice)
  if computerChoice == 'rock':
    print("computer choice is : \n" )
    print(rock)
  elif computerChoice == 'scissors':
    print("computer choice is : \n" )
    print(scissors)
  elif computerChoice == 'paper':
    print("computer choice is : \n" )
    print(paper)
  else:
    print('Ignore A')
  print(f'Your choice is {Player1Selection}')
  print(f'Coumputer choice is {computerChoice}')
  win=sel(Player1Selection,computerChoice )
  if win =='You' or win=='Computer': 
    print(f'{win} win')
  else:
    print('Game is Draw')

elif Player1Selection =="paper":
  print("Your choice is : \n" )
  print(paper)
  computerChoice=""
  computerChoice = random.choice(computerSelection)
  if computerChoice == 'rock':
    print('rock\n')
    print(rock)
  elif computerChoice == 'scissors':
    print("computer choice is : \n" )
    print(scissors)
  elif computerChoice == 'paper':
    print("computer choice is : \n" )
    print(paper)
  else:
    print('Ignore C')
  print(f'Your choice is {Player1Selection}')
  print(f'Coumputer choice is {computerChoice}')
  win=sel(Player1Selection,computerChoice )
  if win =='You' or win=='Computer': 
    print(f'{win} win')
  else:
    print('Game is Draw')
  

elif Player1Selection =="scissors":
  print("Your choice is : \n" )
  print(scissors)
  computerChoice=""
  computerChoice = random.choice(computerSelection)
  if computerChoice == 'rock':
    print("computer choice is : \n" )
    print(rock)
  elif computerChoice == 'scissors':
    print("computer choice is : \n" )
    print(scissors)
  elif computerChoice == 'paper':
    print("computer choice is : \n" )
    print(paper)
  else:
    print('Inore E')
  print(f'Your choice is {Player1Selection}')
  print(f'Coumputer choice is {computerChoice}')
  win=sel(Player1Selection,computerChoice )
  print(win)
  if win =='You' or win=='Computer': 
    print(f'{win} win')
  else:
    print('Game is Draw')
else:
  print("Wrong Choice")
