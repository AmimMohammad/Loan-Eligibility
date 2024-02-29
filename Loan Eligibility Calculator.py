def calculate_monthly_repayment(principal, rate, tenure):
    # Simple interest formula for monthly repayment
    interest = principal * (rate / 100) * (tenure / 12)
    total_repayable = principal + interest
    monthly_repayment = total_repayable / (tenure * 12)
    return monthly_repayment

def check_eligibility(monthly_income, existing_loans, principal, rate, tenure):
    monthly_repayment = calculate_monthly_repayment(principal, rate, tenure)
    total_monthly_obligation = existing_loans + monthly_repayment
    # Check if total monthly obligation is less than 40% of monthly income
    if total_monthly_obligation < monthly_income * 0.4:
        return True
    else:
        return False

# User inputs
monthly_income = float(input("Enter your monthly income: "))
existing_loans = float(input("Enter your existing monthly loan repayment: "))
loan_amount = float(input("Enter desired loan amount: "))
interest_rate = float(input("Enter annual interest rate (as a %): "))
loan_tenure = float(input("Enter loan tenure (in years): "))

# Eligibility check
if check_eligibility(monthly_income, existing_loans, loan_amount, interest_rate, loan_tenure):
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

def adjust_interest_rate_for_tenure(interest_rate, tenure):
    # Simplified logic: longer tenure, slightly higher interest rate
    if tenure > 15:
        return interest_rate + 0.5
    elif tenure > 10:
        return interest_rate + 0.25
    return interest_rate

def credit_score_impact(credit_score):
    # Basic credit score impact on interest rate
    if credit_score < 600:
        return 2.0  # Higher risk, higher interest
    elif 600 <= credit_score < 700:
        return 1.0
    return 0  # Best interest rates for high credit scores

def recommend_max_loan(monthly_income, existing_loans, credit_score):
    # Basic recommendation not to exceed 35% of monthly income for loan repayment
    max_monthly_repayment = monthly_income * 0.35 - existing_loans
    # Adjust based on credit score
    adjustment = credit_score_impact(credit_score)
    max_loan_amount = (max_monthly_repayment / (1 + adjustment / 100)) * 12 * 5  # Assuming a 5-year term for simplicity
    return max_loan_amount

def explore_scenarios(monthly_income, existing_loans, credit_score):
    print("\nExploring different loan scenarios based on your input:")
    for tenure in [5, 10, 15]:
        for amount in [50000, 100000, 150000]:
            rate = adjust_interest_rate_for_tenure(interest_rate, tenure) + credit_score_impact(credit_score)
            eligible = check_eligibility(monthly_income, existing_loans, amount, rate, tenure)
            print(f"Loan Amount: ${amount}, Tenure: {tenure} years, Eligible: {'Yes' if eligible else 'No'}")

# Enhanced user inputs
credit_score = float(input("Enter your credit score: "))
interest_rate = 5.0  # Base interest rate

# Adjust interest rate based on loan tenure and credit score
adjusted_interest_rate = adjust_interest_rate_for_tenure(interest_rate, loan_tenure) + credit_score_impact(credit_score)

# Check eligibility with adjusted interest rate
if check_eligibility(monthly_income, existing_loans, loan_amount, adjusted_interest_rate, loan_tenure):
    print("You are eligible for the loan with the adjusted interest rate.")
else:
    print("You are not eligible for the loan with the adjusted interest rate.")

# Recommend max loan amount
max_loan_recommendation = recommend_max_loan(monthly_income, existing_loans, credit_score)
print(f"Based on your financial health, we recommend a maximum loan amount of: ${max_loan_recommendation:.2f}")

# Explore different scenarios
explore_scenarios(monthly_income, existing_loans, credit_score)



# OUTPUT
# Enter your monthly income: 4500
# Enter your existing monthly loan repayment: 1000
# Enter desired loan amount: 45000
# Enter annual interest rate (as a %): 4
# Enter loan tenure (in years): 20
# You are eligible for the loan.
# Enter your credit score: 7
# You are eligible for the loan with the adjusted interest rate.
# Based on your financial health, we recommend a maximum loan amount of: $33823.53
# 
# Exploring different loan scenarios based on your input:
# Loan Amount: $50000, Tenure: 5 years, Eligible: No
# Loan Amount: $100000, Tenure: 5 years, Eligible: No
# Loan Amount: $150000, Tenure: 5 years, Eligible: No
# Loan Amount: $50000, Tenure: 10 years, Eligible: Yes
# Loan Amount: $100000, Tenure: 10 years, Eligible: No
# Loan Amount: $150000, Tenure: 10 years, Eligible: No
# Loan Amount: $50000, Tenure: 15 years, Eligible: Yes
# Loan Amount: $100000, Tenure: 15 years, Eligible: Yes
# Loan Amount: $150000, Tenure: 15 years, Eligible: No
