import numpy_financial as np

# Original loan details
original_loan_amount = 230415
original_loan_rate = 0.0549
original_loan_term = 15 * 12  # 15 years converted to months
original_monthly_payment = 1881.46
original_current_balance = 208555.87

# Refinanced loan details
refinanced_loan_rate = 0.03
refinanced_out_of_pocket_costs = 2937
refinanced_monthly_payment = np.pmt(refinanced_loan_rate / 12, original_loan_term, -original_current_balance, 0, 0)

# Calculate total cost of original loan
original_total_cost = original_monthly_payment * original_loan_term

# Calculate total cost of refinanced loan
refinanced_total_cost = refinanced_monthly_payment * original_loan_term + refinanced_out_of_pocket_costs

# Calculate present value of savings from refinancing
monthly_inflation_rate = 0.002
savings = 0
for t in range(1, original_loan_term + 1):
    savings += (original_monthly_payment - refinanced_monthly_payment) / ((1 + monthly_inflation_rate) ** t)

# Calculate net savings in current dollars
net_savings = original_total_cost - refinanced_total_cost - savings

# Round net savings to the nearest whole dollar amount
net_savings_rounded = round(net_savings)

print(f"Net savings in current dollars: ${net_savings_rounded}")
