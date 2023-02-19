import pytz

city = input()
for timezone in pytz.all_timezones:
    if city in timezone:
        print(timezone)
else:
    print('False')

print(pytz.all_timezones)