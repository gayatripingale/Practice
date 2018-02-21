 # This code is to find the sum of all values given in arrey or list format as a value of a key 

# monthly_takings = {'January': [54, 63]}

# to find the total of list of  'value' s in an array
# of a key 'January'.
# i.e. the output should be sum of 
# 54,63,75,64,60,63, 49,57 and 42

#monthly_takings = {'January':[54, 63, 75],'February': [64, 60], 'March': [63, 49],
#'April': [57, 42]}
# Here we willneed 2 variables: One for Key i.e. Months-Jan till Dec
# And, second one for Value i.e list of numbers

def total_takings(monthly_takings):
    total = 0
    for month in monthly_takings:
        length = len(monthly_takings[month])
        for i in range(length):
            total += monthly_takings[month][i]
            i += 1
        print("Monthaly Total is:",total)
    return total

print("Yearly total is:",total_takings({'January':[54, 63, 75],'February':[64, 60],'March':[63, 49], 'April':[57,42]}))

