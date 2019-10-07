# Calculate number of days between 2 dates
class Solution(object):
    def __init__(self):
        self.daysOfMonth = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11: 30, 12:31}
        
    def isLeapYear(self, year):
        if(year%4 == 0):
            return True
        return False
    
    def getYearMonthDay(self, date):
        splitDate = date.split("/")
        return int(splitDate[2]), int(splitDate[0]), int(splitDate[1])

    def getDaysFrom1stJan(self, day, month, year):
        # if current year is leap year then change days in feb
        if(self.isLeapYear(year)):
            self.daysOfMonth[2] = 29
        days = 0
        # calculate days
        for i in range(1, month):
            days = days + self.daysOfMonth[i]
        # add current day to get number of days till now in this year
        return days+day

    def getDaysFromBeginningOfTime(self, year):
        days = 0
        for i in range(year):
            if(self.isLeapYear(i)):
                days = days+366
            else:
                days = days+365
        return days
        
    def getDays(self, date):
        year, month, day = self.getYearMonthDay(date)
        # calculate days from 1st jan to now
        d1 = self.getDaysFrom1stJan(day, month, year)
        # calculate days of all years from 0000
        d2 = self.getDaysFromBeginningOfTime(year)
        return d1+d2
        
    def numberOfDays(self, date1, date2):
        d1 = self.getDays(date1)
        d2 = self.getDays(date2)
        # the difference between 2 dates
        print abs(d2-d1),"days"

# Main
obj = Solution()
# please enter date in MM/DD/YYYY format
obj.numberOfDays("2/1/2000", "2/1/2004")
