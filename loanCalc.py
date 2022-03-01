# LOAN CALCULATOR
# GET THE LOAN DETAILS

money_owed = float(input('How much money do you owe?\n')) # $50,0000
apr = float(input('What is the annual % rate?\n')) # 3%
payment = float(input('What will your monthly payment be?\n')) # $1,000
months = int(input('How many months do you want to see results for?\n')) # 24

# DIVIDE APR BY 100 TO MAKE IT A PERCENT, THEN DIVIDE BY 12 TO MAKE MONTHLY PAYMENTS
monthly_rate = apr/100/12

for i in range(months):
    # ADD IN INTEREST
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break
    # MAKE PAYMENT
    money_owed = money_owed - payment

    # PRINT RESULTS
    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now I owe', money_owed)

