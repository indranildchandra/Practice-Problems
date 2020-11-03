
# Given standard denominations list in bank - 1,2,5,10, withdraw x amount 
# Requirement -> Find out minimum number of denominations and count for each 
# Constraint 1 -> Remove 1 from sample test case - not all possible values can be satisfied
# Constraint 2 -> Check for arbitrary denominations

def get_currency_count(sum_amount, notes):
    amount = sum_amount
    notes.sort(reverse=True)
    currency_count = list()
    if notes is None or amount is None or amount < min(notes):
        return list(), False
    else:
        # print ("Currency Count: ") 
        for counter, note in enumerate(notes):
            if amount >= note: 
                count = amount // note 
                amount = amount - (count * note)
                # print(str(note) + ": " + str(count))
                currency_count.append((note, count))
        if get_currency_count_sum(currency_count) != sum_amount:
            return list(), False
    return currency_count, True


def get_currency_count_sum(currency_count_arr):
    # print(currency_count_arr)
    sum = 0
    for currency_count in currency_count_arr:
        sum += currency_count[0] * currency_count[1]
    return sum


## Test Case 1
amount = 868
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
print("Denominations: {}".format(notes))
currency_count, success_flag = get_currency_count(amount, notes)
print("Successfull Evaluation Flag: {}".format(success_flag))
print("Solution: {}".format(currency_count))
calculated_currency_count_sum = get_currency_count_sum(currency_count)
print("Required Currency Count Sum: {}".format(amount))
print("Calculated Currency Count Sum: {}".format(calculated_currency_count_sum))
print("Valid Result: {}".format(amount == calculated_currency_count_sum))
print("-----------------------------------------------------------------")

## Test Case 2
amount = 2
notes = [1, 2,4,6]
print("Denominations: {}".format(notes))
currency_count, success_flag = get_currency_count(amount, notes)
print("Successfull Evaluation Flag: {}".format(success_flag))
print("Solution: {}".format(currency_count))
calculated_currency_count_sum = get_currency_count_sum(currency_count)
print("Required Currency Count Sum: {}".format(amount))
print("Calculated Currency Count Sum: {}".format(calculated_currency_count_sum))
print("Valid Result: {}".format(amount == calculated_currency_count_sum))
print("-----------------------------------------------------------------")

## Test Case 3
amount = 3
notes = [2,4,6]
print("Denominations: {}".format(notes))
currency_count, success_flag = get_currency_count(amount, notes)
print("Successfull Evaluation Flag: {}".format(success_flag))
print("Solution: {}".format(currency_count))
calculated_currency_count_sum = get_currency_count_sum(currency_count)
print("Required Currency Count Sum: {}".format(amount))
print("Calculated Currency Count Sum: {}".format(calculated_currency_count_sum))
print("Valid Result: {}".format(amount == calculated_currency_count_sum))
print("-----------------------------------------------------------------")

## Test Case 4
amount = None
notes = [2,4,6]
print("Denominations: {}".format(notes))
currency_count, success_flag = get_currency_count(amount, notes)
print("Successfull Evaluation Flag: {}".format(success_flag))
print("Solution: {}".format(currency_count))
calculated_currency_count_sum = get_currency_count_sum(currency_count)
print("Required Currency Count Sum: {}".format(amount))
print("Calculated Currency Count Sum: {}".format(calculated_currency_count_sum))
print("Valid Result: {}".format(amount == calculated_currency_count_sum))
print("-----------------------------------------------------------------")