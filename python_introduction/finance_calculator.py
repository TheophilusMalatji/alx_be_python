income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

savings = income - expenses
psavings:int = int(savings * 12 + (savings * 12 * 0.05))

print(f'Projected savings after one year, with interest, is: ${psavings}')