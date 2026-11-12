#Task 1
loan_amount = float(input("Enter the loan amount: "))
years = int(input("Enter the number of years: "))
month = years * 12
principal = loan_amount / month
remaining_balance = loan_amount

for x in range (1,month + 1):
    remaining_balance -= principal
    loan_interest = remaining_balance * 0.00256
    monthly_pay = loan_interest + principal
    print(x, round(loan_interest, 2),round(principal, 2),round(monthly_pay, 2), round(remaining_balance, 2))

#Task 2
for x in range (7):
    for y in range (13):
        if x == 6 or y - x == 6 or x+ y == 6 or x + y == 18:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")

#Task 3
for x in range (5):
    for y in range (5):
        if x == 0 or x == 4 or x+y == 4:
            print("*", end = "")
        else:
            print(" ", end = "")
    print (" ")






