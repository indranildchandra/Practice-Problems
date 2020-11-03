# Spare-cash problem
# You have a saving account with starting(start of month) balance B = 300
# Income list I = [(5, 100), (10, 200)] --> (date,amount)
# Expense list E = [(7, 150), (9, 50), (12, 150)] --> (date,amount)
# Spare cash S, maximum giveaway amount on start of month, without you going into negative balance.
B = 300
I = [(5, 100), (10, 200)]
E = [(7, 150), (9, 50), (12, 150)]

balance = [0]*31
balance[0] = B
count = 1
income_list = dict(I)
expense_list = dict(E)
print("Balance as of day {} is {}".format(0, balance[0]))
for day in range(1, 31):
    income = income_list.get(day) if day in income_list.keys() else 0
    expense = expense_list.get(day) if day in expense_list.keys() else 0
    balance[count] = balance[count-1] + income - expense
    print("Balance as of day {} is {}".format(day, balance[count]))
    count += 1
output = min(balance)
print("Minimum Spare Cash that needs to be maintained: {}".format(output))