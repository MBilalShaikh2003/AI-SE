from datetime import datetime
currenttime=datetime.now()
getyear=lambda dt:dt.year
getmonth=lambda dt:dt.month
getday=lambda dt:dt.day


print("Current Date and Time:", currenttime)
print("Year:", getyear(currenttime))
print("Month:", getmonth(currenttime))
print("Day:", getday(currenttime))