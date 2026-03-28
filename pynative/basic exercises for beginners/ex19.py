"""Multi-Tiered Income Tax Calculation."""

"""Calculate income tax for given income based on this rules.
Rules:
1. First $10_000 : 0% tax
2. Next $10_000 : 10% tax
3. remaining_income : 20% tax

pseudocode

BEGIN

BALANCE AS A NUMBER INPUT
TOTAL_TAX = 0
# BASE CONDITION 0 %
IF BALANCE > 10000:
    BALANCE = BALANCE - 10_000

# SECOND CONDITION NEXT 10000
IF BALANCE > 10_000:
    BALANCE = BALANCE - 10_000
    TAX = 10_000 * 10 / 100
    TOTAL_TAX = TOTAL_TAX + TAX
ELSE:
    TAX = BALANCE * 10 / 100
    TOTAL_TAX = TOTAL_TAX + TAX
    BALANCE = 0

IF BALANCE:
    TAX = BALANCE * 20 / 100
    TOTAL_TAX = TOTAL_TAX + TAX

PRINT TOTAL_TAX
"""

def calculate_tax(principal_amount):
    total_tax = 0
    balance = principal_amount

    # base condition
    if balance > 10_000:
        balance = balance - 10_000

    # second condition
    if balance > 10_000:
        balance = balance - 10_000
        tax = 10_000 * 10 / 100
        total_tax += tax
    else:
        tax = balance * 10 / 100
        total_tax += tax
        balance = 0
    
    # third condition
    if balance:
        tax = balance * 20 / 100
        total_tax += tax
    
    return total_tax


result = calculate_tax(22000)

print(result)