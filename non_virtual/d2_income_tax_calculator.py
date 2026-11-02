base_income: float = float(input('Enter your base income: '))
double: float = 2 * base_income
triple: float = 3 * base_income
tax_rate: float = float(input('Enter your tax rate: ')) / 100
taxed: float = float(base_income * tax_rate)
d_taxed: float = float(double * tax_rate)
t_taxed: float = float(triple * tax_rate)

print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:               $ {base_income:.2f}')
print(f'Base Income (Doubled):     $ {double:.2f}')
print(f'Base Income (Trippled):    $ {triple:.2f}')
print(f'Tax Rate:                  {tax_rate:.0%}')
print('-' * 40)
print(f'Yearly taxed (Base):       $ {taxed:.2f}')
print(f'Yearly taxed (Doubled):    $ {d_taxed:.2f}')
print(f'Yearly taxed (Trippled):   $ {t_taxed:.2f}')
print('=' * 40)
