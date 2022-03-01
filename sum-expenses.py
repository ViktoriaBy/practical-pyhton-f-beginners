# CALCULATE EXPENSES

expenses = [10.50, 8, 5, 15, 20, 5, 3]
# full_sum = 0
#
# for x in expenses:
#     full_sum = full_sum + x

total = sum(expenses)

print('You spent $', total, sep='') #sep means remove the space

# RANGE(7) OR RANGE(0,7,1) FUNCTION GENERATES SEQUENCES (0,1,2,3,4,5,6)
# RANGE(2,14,2) -> (2,4,6,8,12)

total = 0
expenses = []

for i in range(7):
    expenses.append(float(input('Enter an expense:')))
total = sum(expenses)

print('You spent $', total, sep='')