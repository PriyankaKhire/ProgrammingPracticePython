import datetime
import calendar
from dateutil import relativedelta

def getDateTimeObj(dateString):
    try:
        dateTimeObj = datetime.datetime.strptime(dateString, "%m/%d/%Y")
    except:
        print "Entered wrong date"
        return 
    return dateTimeObj

def monthlySchedule(dateString):
    dateTimeObj = getDateTimeObj(dateString)
    print (dateTimeObj + relativedelta.relativedelta(months=1, day=15))

def semiMonthlySchedule(dateString):
    daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dateTimeObj = getDateTimeObj(dateString)
    weekDay = daysOfWeek[dateTimeObj.weekday()]
    print weekDay
    if (weekDay == 'Wednesday' or weekDay == 'Thursday' or weekDay == 'Friday'):
        print dateTimeObj + relativedelta.relativedelta(days=+1, weekday=calendar.WEDNESDAY)
    if (weekDay == 'Saturday'):
        print dateTimeObj + relativedelta.relativedelta(days=+1, weekday=calendar.FRIDAY)
    else:
        print dateTimeObj + relativedelta.relativedelta(days=+7, weekday=calendar.FRIDAY)

# Main
#monthlySchedule("02/28/2024")
semiMonthlySchedule("04/21/2024")

# mm/dd/yyyy
given_date = datetime.datetime.strptime("12/31/2023", "%m/%d/%Y")
# mm/dd/yy
given_date = datetime.datetime.strptime("4/4/24", "%m/%d/%y")
#print given_date.weekday()
