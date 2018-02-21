# This code is to find the sum of all values given in arrey or list format as a value of a key 

# monthly_takings = {'January': [54, 63]}

# to find the total of 'value' in a arry form [54,63]
# of a key 'January'.
# i.e. the output should be 54 + 63 = 117


monthly_takings = {'January':[54, 63, 75]}

total = 0

length = (len(monthly_takings['January']))

for i in range(length):
    total += monthly_takings['January'][i]
    i += 1
print("total of all values assigned to a key January is :", total)    











