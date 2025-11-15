import datetime

t = datetime.datetime.now()
present_year = int(t.strftime("%Y"))

birth_year = int(input("Enter your birth year: "))

age = present_year - birth_year

print("Your age is:", age)
