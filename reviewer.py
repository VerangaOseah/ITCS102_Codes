#Reviewer
age = int(input("Age: "))
monthly_revenue = float(input("Monthly Revenue: "))
credit_score = int(input("Credit Score: "))
business_years = float(input("Years in Business "))
has_defaults = bool(input("Has Defaults True or False? "))
collateral_name = input("Collateral Name: ")
collateral_value = float(input("Collateral Value: "))

max_loan = 0
base_fee = 0

if age >= 21 and business_years >= 2.0 and has_defaults == False:
    print("Baseline Passed") 

    if credit_score >= 720:
        max_loan = monthly_revenue * 3
        if monthly_revenue >= 5000:
            base_fee = max_loan * 0.015
            print ("Base fee is set to ",base_fee)
        else:
            base_fee = max_loan * 0.025
            print("Base fee is set to ",base_fee)

    elif credit_score <= 620 and credit_score < 720:
        print("Credit score is within range of 620 - 720")
        max_loan = monthly_revenue * 1.5
        if business_years >= 5.0:
            base_fee = max_loan *0.02
            print("Years in Business greater than 5 years base fee is ", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("Years in Business lower than 5 years base fee is ",base_fee)

    elif credit_score < 620:
        print("Credit score is too low")

    


            

    else:
        print("INVALID")




else:
    print("Baseline Denied")