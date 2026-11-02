from typing import Final
import random

LOWER_LIMIT: Final[int] = 0
UPPER_LIMIT: Final[int] = 100

radom_number: int = random.randint(LOWER_LIMIT, UPPER_LIMIT)

def bot_message(msg: str) -> None:
    print(f'Bot: {msg}')

bot_message('Welcome to Guess that Numbers !')
bot_message(f'Guess a number from {LOWER_LIMIT} to {UPPER_LIMIT}')
count: int = 0
while True: 
    try:
        user_guess: int = int(input('You: '))
    except ValueError as e:
        bot_message(f'{e}, please enter number only')
        continue

    if user_guess > radom_number:
        count += 1
        bot_message('The number is lower')
    elif user_guess < radom_number:
        count += 1
        bot_message('The number is higher')
    else:
        bot_message(f'You guessed the number in {count + 1} tries. You win!')
        break