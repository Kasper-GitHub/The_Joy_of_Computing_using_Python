from datetime import datetime
import pytz

timezones = pytz.all_timezones

for i in range(len(timezones)):
    zone = timezones[i]
    tz = pytz.timezone(zone)
    print("Current time at timezone : ", zone, " is ", datetime.now(tz))