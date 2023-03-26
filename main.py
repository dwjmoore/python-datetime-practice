from datetime import datetime

birthday = datetime(1980, 3, 30, 3, 30)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.weekday())

print(datetime.now())

print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018, 1, 1))

parsed_date = datetime.strptime("Jan 15, 2018", "%b %d, %Y")
print(parsed_date.month)
print(parsed_date.year)