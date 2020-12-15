import datetime
today=datetime.date.today() # print today date
print(today)

# datetime.timedelta(days=10)
tdelta= datetime.timedelta(days=10)
print(today-tdelta)  # it gives day before 10 days from current days
print(today+tdelta)  # it gives day after 10 days from current days

print(today.day) #it print today date
print(today.weekday()) # it print day of the week
""" day of the week start from monday=0, sunday=6
"""

#datetime.datetime.now() print current time now
time_now=datetime.datetime.now()
print(time_now)

hours_delta=datetime.timedelta(hours=10)
print(time_now+hours_delta)  // it add 10 hours to current days