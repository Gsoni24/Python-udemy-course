# 1.
print('Welcome to Expense Splitter!')
while True:
  total_bill:str = input('1. Enter the total bill you want to split: ')
  if total_bill.strip() == "":
    print("Please enter total bill amount")
  else:
    bill = float(total_bill)
    break

# 2.
while True:
  people: list[str] = []
  print('2. Add the participants (press Enter on an empty line when finished): ')
  while True:
    input_name: str = input('Names: ').lower()
    if input_name.strip() == '':
      break

    if input_name in people:
      print(f'{input_name} is already present')
    else:
      people.append(input_name)
  if people == []:
    print('You Have to add atleast one participant')
  else:
    break

# 3.

print('3. Now specify the percentage each person will pay.')
print('(type "even" at any time to split the bill equally.)')

people_dict: dict[str, float] = {}
total_percent: float = 100.0

for person in people:
  percent_input: str = input(f'[{total_percent:.0f}%] remaining {person.capitalize()}: ').lower()

  if percent_input.strip() == '':
    percent_input = '0'

  if percent_input.strip() == 'even':
    for nested_person in people:
      people_dict[nested_person] =  (1 / len(people)) * bill
    break

  people_dict[person] = (float(percent_input)/ 100) * bill

  total_percent -= float(percent_input)


# 4.
print('\n----- Split Summary')

for name, share in people_dict.items():
  print(f'{name.capitalize():10}: ${share:,.2f}')
print('----------------------')
