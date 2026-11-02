import matplotlib.pyplot as plt

#Main data
monthly_income: float = 10000
rent: float = 1000
food: float = 2500
tax_rate: float = 0.22
taxes: float = monthly_income * tax_rate
other_expenses: float = 2000

yearly_income: float = monthly_income * 12
yearly_expenses: float = sum([rent, food, taxes, other_expenses] * 12)
yearly_savings: float = yearly_income - yearly_expenses

#data for plotting
monthly_categoreis : list[str] = ['Income', 'Rent', 'Food', 'Taxes', 'Other']
monthly_amounts : list[float] = [monthly_income, rent, food, taxes, other_expenses]
monthly_colors : list[str] = ['green', 'red','red', 'red', 'red']

yearly_categoreis : list[str] = ['Income', 'Expenses', 'Savings']
yearly_amounts : list[float] = [yearly_income, yearly_expenses, yearly_savings]
yearly_colors : list[str] = ['green', 'red','green']

fig, axes = plt.subplots(1,2, figsize=(10, 6))

axes[0].bar(monthly_categoreis, monthly_amounts, color=monthly_colors)
axes[0].set_title('Monthly Financial Overview')
axes[0].set_ylabel('Amount ($)')
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(yearly_categoreis, yearly_amounts, color=yearly_colors)
axes[1].set_title('Yearly Financial Overview')
axes[1].set_ylabel('Amount ($)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()