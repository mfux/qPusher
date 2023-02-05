import pytz
import datetime as dt
from time import sleep

def berlin_now():
    berlin_tz = pytz.timezone("Europe/Berlin")
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    berlin_now = utc_now.astimezone(berlin_tz)
    return berlin_now

#31.03.2019 um 2:00 Uhr. Die Uhr wird dann um 1 Stunde vorgestellt
berlin_tz = pytz.timezone("Europe/Berlin")
umstellung = berlin_tz.localize(dt.datetime(year=2019, day=31, month=3, hour=2, second=0))

time_str = "%d.%m.%Y, %H:%M:%S"
# main
start = umstellung - dt.timedelta(seconds=5)
now = start.astimezone(pytz.utc)
for i in range(10):
    print(now.astimezone(berlin_tz).strftime(time_str))
    now = now + dt.timedelta(seconds=1)
    sleep(1)
