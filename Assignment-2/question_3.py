'''Given the month and year as numbers, return whether that month contains a Friday 13th.(i.e You can check Python's datetime module)

Examples

has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False

'''

from datetime import datetime
import calendar

def has_friday_13(month,year):
    date=str(13)+str(month)+str(year)
    day=datetime.strptime(date,'%d%m%Y').weekday()
    #print(calendar.day_name[day])
    if calendar.day_name[day].lower()=='friday':
        print(True)
    else:
        print(False)    


has_friday_13(3, 2020) 

has_friday_13(10, 2017)

has_friday_13(1, 1985) 
   