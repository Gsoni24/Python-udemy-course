import random

symbols: dict[str, str] = {'rock': '🪨', 'paper': '📄', 'scissors':'✂️'} 
while True:
  choice: str= input('Play Again (y/n): ').strip().lower()
  if choice == 'y':

    player_choice: str = input('Choose rock (🪨), paper(📄), or scissors (✂️):').strip().lower()
    computer_choice: str = random.choice(tuple(symbols))

    print('\n Results: ')
    print('---------------')
    print(f'You:         {symbols[player_choice]}{player_choice}')
    print(f'Computer:    {symbols[computer_choice]}{computer_choice}')
    print('---------------')

    if player_choice == computer_choice:
      print('It is a Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
      print('You Win with rock! 🪨')
    elif player_choice == 'paper' and computer_choice == 'rock':
      print('You Win with Paper! 📄')
    elif player_choice == 'scissors' and computer_choice == 'paper':
      print('You Win with Scissors! ✂️')
    else:
      print('Computer Wins! 🤖')
  elif choice == 'n':
    print('Thank you for playing!')
    break

  else:
    print('Invalid Choice')
