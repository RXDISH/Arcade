import random

print('Welcome to the slots!')
print('')
print('In order to win, you gotta line up a 777')
print('Like this! 7️⃣  |7️⃣ |7️⃣')
print('Good luck, you\'re gonna need it')
print('')

def play():
  symbols = ['🍒', '🍇', '🍉', '7️⃣']

  results = random.choices(symbols, k=3)
  print(f'{results[0]} | {results[1]} | {results[2]}')
  print('')

  if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
    print('You win! :D')
  else:
    print('L bozo')
    print('')

answer = ''
while answer.upper() != 'N': # 'upper' makes any input by a user into uppercase
  play()
  answer = input('Keep playing? (Y/N) ')