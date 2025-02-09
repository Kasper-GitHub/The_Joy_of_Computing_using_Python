import random
import datetime

birthdays = []
i = 0

while i < 50:
    year = random.randint(1968, 2024)
    if year % 4 == 0 and year % 100 or year % 400 == 0:
        leap = 1
    else:
        leap = 0

    month = random.randint(1,12)
    if month == 2 and leap ==1:
        day = random.randint(1,29)
    elif month == 2 and leap ==0:
        day = random.randint(1,28)
    elif month == 7 or month == 8:
        day = random.randint(1,31)
    elif month % 2 != 0 and month < 7:
        day = random.randint(1,31)
    elif month % 2 == 0 and 7 < month < 12:
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)

    dd = datetime.date(year,month,day)
    day_of_year = dd.timetuple().tm_yday

    i += 1
    birthdays.append(day_of_year)

birthdays.sort()

j = 0
frequency = []
while j < 50:
    frequency.append(birthdays.count(birthdays[j]))
    j += 1

distribution = dict(zip(birthdays, frequency))

matching_day = [[key, value] for (key, value) in distribution.items() if value > 1]

print("Matching Birthdays are:")
for i in matching_day:
    date = datetime.datetime(dd.year,1, 1) + datetime.timedelta(i[0] - 1)
    print(date.strftime("%d-%m-%Y"),"occurring", i[1],"times")