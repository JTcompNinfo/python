'''
Program taxform.py
Author: Joel Dinovo

Computer a person's income tax
1. Significant constatnt
    tax rate
    standard deduction
    deduction per dependent
2. the inputs are:
    gross income
    numbers of depenents
3. computations:
    taxable income = gross income - the standard deduction - a deduction for each dependent
    income tax = is a fixed percentage of the taxable income
4. the outputs areL
    the income tax
'''

# Initialize the constant
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DECUCTION = 1000.0

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependent = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DECUCTION * numDependent

incomeTax = taxableIncome * TAX_RATE

#display the income tax
print("The income tax is $" + str(incomeTax))
