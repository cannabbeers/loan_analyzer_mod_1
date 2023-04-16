# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
# count_loans = len(loan_costs)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE! 
# total_lent = sum(loan_costs)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
# avg_loan_size = total_lent / count_loans

count_loans = len(loan_costs)
total_lent = sum(loan_costs)
avg_loan_size = total_lent / count_loans

def underline(text):
    print("\u0332".join(text))

print("\n")
underline("\tMODULE 1 CHALLENGE\n")
print("Part 1: Automate the Calculations\n")     
print(f"\tThere are {count_loans} loans in this portfolio.")
print(f"\tTotal amount lent out by this portfolio is $ {total_lent:,.2f}")
print(f"\tThe average loan size in this portfolio is $ {avg_loan_size:,.2f}\n")


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`. 
    b. Print each variable. 

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.

3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.

    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!
# future_value = loan.get("future_value")
# remaining_months = loan.get("remaining_months")
# print(f"\t1. The 'Future Value' of the loan is $ {future_value:,.2f}")
# print(f"\t2. There are {remaining_months} months left until this loan matures.")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.  *** SEE LINE 76
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
#  
# YOUR CODE HERE!
# discount_rate = 0.20 
# present_value = future_value / (1 + discount_rate / 12) ** remaining_months
# def fair_value_calculator(future_value, annual_rate, months_remaining):
#     return future_value / (1 + annual_rate / 12) ** months_remaining

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE! 
# if present_value <= future_value:
#         print(f"Since the 'Fair Value' is $ {future_value - present_value:,.2f} less than its 'Future Value' of $ {future_value:,.2f} at maturity,\n")
#         print(f"The loan is worth at least the cost to buy for $ {present_value:,.2f}, which is it's 'Present Value' today.\n")
# else:
#         print(f"Since the 'Fair Value' of the loan today is more than its 'Future Value' of $ {future_value:,.2f} at maturity.\n")
#         print("The loan is too expensive and not worth the price.")

loan_sample = loan.get("loan_price")
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

discount_rate = 0.20 
present_value = future_value / (1 + discount_rate / 12) ** remaining_months

def fair_value_calculator(future_value, annual_rate, months_remaining):
    return future_value / (1 + annual_rate / 12) ** months_remaining

print("Part 2: Analyze Loan Data\n")
print("\tGIVEN LOAN DATA:\n")
print(f"\t1. The 'Future Value' of the loan is $ {future_value:,.2f}")
print(f"\t2. There are {remaining_months} months left until this loan matures.")
print(f"\t3. The 'Annual Interest Rate' of the $ {loan_sample:,.2f} loan is {100 * discount_rate}%\n")
print(f"\tThe 'Present Value' of the loan is $ {present_value:,.2f} which is a.k.a its 'Fair Value'\n")
print(f"\tTherefore the 'Fair Value' of this loan is $ {present_value:,.2f}\n")

if present_value <= future_value:
        print(f"\tSince the 'Fair Value' is $ {future_value - present_value:,.2f} less than its 'Future Value' of $ {future_value:,.2f} at maturity,\n")
        print(f"\tThe loan is worth at least the cost to buy for $ {present_value:,.2f}, which is it's 'Present Value' today.\n")
else:
        print(f"\tSince the 'Fair Value' of the loan today is more than its 'Future Value' of $ {future_value:,.2f} at maturity.\n")
        print("\tThe loan is too expensive and not worth the price.")


"""

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE! 
# present_value = future_value / (1 + discount_rate / 12) ** remaining_months
# def fair_value_calculator(future_value, annual_rate, months_remaining):
#     return  future_value / (1 + annual_rate / 12) ** months_remaining

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE! 
# new_present_value = fair_value_calculator(new_loan_future_value, discount_rate, new_loan_remaining_months)

new_loan_sample = new_loan.get("loan_price")
new_loan_remaining_months = new_loan.get("remaining_months")
new_loan_future_value = new_loan.get("future_value")
new_loan_costs = new_loan.get("loan_price")
new_present_value = fair_value_calculator(new_loan_future_value, discount_rate, new_loan_remaining_months)

print("Part 3: Perform Financial Calculations\n")
print("\tGIVEN LOAN DATA:\n")
print(f"\t1. The 'Future Value' of the loan is $ {new_loan_future_value:,.2f}")
print(f"\t2. There are {new_loan_remaining_months} months left until this new loan matures.")
print(f"\t3. The 'Annual Interest Rate' of the new loan for $ {new_loan_sample:,.2f} is {100 * discount_rate}%\n")
underline(f"\tSOLUTION:\n")
print(f"\tThe present value of the new loan is: ${new_present_value:,.2f}\n")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]



# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = [] #  <-- empty list
loan_index = [] #  <-- empty list

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

for chk_price in loans:     
    if chk_price['loan_price'] <= 500:
        # inexpensive_loans.append(price['loan_price'])
        inexpensive_loans.append(chk_price)
        loan_index.append(loans.index(chk_price))

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!
print("Part 4: Conditionally filter lists of loans\n")
count_items_in_loans = len(loans)
count_loan_index = len(loan_index)

print(f"\tFirst we are given a loan inventory to evaluate to determine which loans are 'inexpensive'.")
print(f"\t'Inexpensive' is defined as having a 'loan price' less than or equal to $500")
print(f"\tThe inventory is in the form of a list of {count_items_in_loans} loans.\n")
print("\tTo solve, we iterate over the list to find the 'inexpensive loans'.\n") 
print(f"\tThe {count_loan_index} 'inexpensive loans' in the portfolio are:\n")

for price_only in inexpensive_loans:
    print("\t$ {}".format(price_only["loan_price"])) 

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects
"""
# Set the output header
# header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
# output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

print("\n")
print("Part 5: Save the results\n")

print("The final step in this challenge is to save our results by writing a .csv file named 'inexpensive_loans.csv'\n")

print(f"From the original {count_items_in_loans} loans in the given portfolio, we are asked to save the 'inexpensive loans' only.\n")

underline(f"... SAVING THE '{count_loan_index} inexpensive loans' shown below using csv module in Python.\n")

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")

csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as inexpensive_csv:
    csv_writer = csv.writer(inexpensive_csv)
    csv_writer.writerow(header)             # this line creates the 'header' in the csv file
    for row in inexpensive_loans:
        csv_writer.writerow(row.values())   # this line saves the 'inexpensive loans in the .csv
        print(row)                          # this line prints the 'inexpensive loans' into the terminal terminal window

