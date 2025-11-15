
import datetime

n = datetime.datetime.now()

print(n)


# Year
print(n.strftime("%y"))
print(n.strftime("%Y"))


# Month
print(n.strftime("%b"))
print(n.strftime("%B"))
print(n.strftime("%m"))


# Day
print(n.strftime("%a"))
print(n.strftime("%A"))
print(n.strftime("%j"))


#Dayname from date
import calendar
weekday = calendar.weekly

dayname = calendar.day_name[weekday]

print(dayname)
