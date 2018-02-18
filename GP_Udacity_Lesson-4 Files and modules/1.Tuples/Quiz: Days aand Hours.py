"""
Quiz: Days nd Hours

Try your hand writing a funstion that uses a tuple to return multiple values
Write an " hours2days" function that takes ne argument an integer
that is time perios in hours.
The func should return a tuple of how long that perios is in days and hrs
with hrs being the remainder that can't be expressed in days.
EX: 39 hrs is 1 day and 15 hrs. so the func should return (1,15).

hours2days(24) should return (1,0)
hours2days(25) shuold return (1,1)
hours2dys(10000) should return(416,16)... and so on
"""
def hours2days(period):
    #days = int(period / 24)
    #hours = period % 24
    return int(period / 24), period % 24
print("(days, hours):",hours2days(25))





