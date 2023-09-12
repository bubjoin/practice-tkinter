
import datetime

delta = datetime.timedelta(
    days=365,
    hours=0,
    minutes=0,
    seconds=0,
    microseconds=0
)

print(delta.total_seconds())

two_years = delta * 2
print(two_years)

utc = datetime.datetime.now(datetime.timezone.utc)
print(utc)

# pip install tzdata
import zoneinfo

kor = datetime.datetime.now(zoneinfo.ZoneInfo("Asia/Seoul"))
print(kor)

availables = list(zoneinfo.available_timezones()) # set is not subscriptable
print(len(availables))

print(utc + two_years)
print(kor + two_years)