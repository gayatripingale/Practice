# A regular flying circus happens twice or thrice a month
# The amount of money taken at each event is stored in a list 
# so that the amount appear in the order it happened
# 'monthly_takings'--> is a dictionay in which The monthly data was collected.
# 'total_takings()--> is the function that calculates the sum of takings from 
# every circus in the year.
# To do : Write down the code in which calculates
# the sum of the takings from every circus in th eyear 
# monthly_takings ={'January': [54, 63], 'February': [64, 60], 
#                     'March': [63, 49],'April': [57, 42], 
#                     'May': [55, 37], 'June': [34, 32], 
#                    'July': [69, 41,42],'August': [40, 61, 40], 
#                 'September': [51, 62], 'October': [34, 58, 45], 
#            'November': [67, 44], 'December': [41, 58]}


def total_takings(monthly_takings):
    total = 0
    for month in monthly_takings:
        length = len(monthly_takings[month])
        for i in range(length):
            total += monthly_takings[month][i]
            i += 1
        print("Takings for the month of ",month + " is:",total)      
    return total

print("\n Yearly total taking is :",total_takings({'January': [54, 63], 'February': [64, 60], 
                    'March': [63, 49],'April': [57, 42],
                     'May': [55, 37], 'June': [34, 32], 
                  'July': [69, 41,42],'August': [40, 61, 40], 
                'September': [51, 62], 'October': [34, 58, 45], 
             'November': [67, 44], 'December': [41, 58]}))