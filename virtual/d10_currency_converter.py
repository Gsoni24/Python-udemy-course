import json

def load_exchange_rate() -> dict[str, float]:
    with open('curriencies.json_10',  'r') as file:
        return json.load(file)

def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available curreincies.')
    print('3. Type QUIT to exit')

def convert(user_input: str, rates: dict[str, float]) -> None:
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]

    if input_currency_code not in currency_codes:
        print(f'Currecy code: {input_currency_code} is invalid.')
        return

    try:
        input_amount: float = float(user_input[:-3])
    except ValueError:
        print(f'{user_input} is invalid. Try something like "10 AUD"')
        return

    base_conversion: float = input_amount/ rates[input_currency_code]

    print(f'{round(input_amount, 2):>16} {input_currency_code}')
    print('-'*20)

    for currency_code in currency_codes:
        converted_amount: float = base_conversion * rates[currency_code]
        print(f'= {round(converted_amount, 2):>14} {currency_code}')
    print('-'*20)


def main() -> None:
    instructions()

    exchange_rates: dict[str, float] = load_exchange_rate()

    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {', '.join(exchange_rates.keys())}')
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        convert(user_input, exchange_rates)

if __name__ == '__main__':
    main()
