import time

# convert from ... to ...
#
# 1. time.struct_time or the tuple of it
# 2. string or formatted string
# 3. seconds since epoch
#
# epoch : 1970. 1. 1. 00:00:00 3 1 0

print("\n[ time.time() -> float, current time in seconds since epoch ]")
print(time.time()) # current time in seconds since epoch
print(type(time.time())) # float


print("\n[ time.gmtime(seconds since epoch) -> time.struct_time in utc ]")
print(time.gmtime(time.time())) # current time to utc, same result without arg
print(time.gmtime()) # convert current time to utc
print(type(time.gmtime())) # the return type is time.struct_time

print(time.gmtime(60*60*24)) # convert seconds since epoch given to utc
print(time.gmtime(0)) # epoch in all platforms, 1970. 1. 1. 00:00:00 3 1 0


print("\n[ time.sleep(seconds) -> delay for seconds ]")
time.sleep(0.5) # delay current thread for seconds given


print("\n[ time.ctime(seconds since epoch) -> str, local time string ]")
print(time.ctime(60*60*24)) # seconds since epoch to local time string
print(type(time.ctime(60*60*24)))


print("\n[ time.localtime(seconds since epoch) -> time.struct_time in utc ]")
print(time.localtime(60*60*24)) # seconds since epoch to local time
print(type(time.localtime(60*60*24)))
print(time.localtime(time.time()))


print("\n[ time.mktime(time.struct_time or the tuple in localtime) \
-> seconds since epoch ]")
print(time.mktime((1970, 1, 1, 9, 0, 0, 3, 1, 0))) # -1 dst flag, if unknown


print("\n[ local time to utc ]")
print(time.gmtime(time.mktime((1970, 1, 1, 9, 0, 0, 3, 1, 0))))


print("\n[ convert utc to seconds since epoch, the 2 ways ]")
print("[ # 1: calendar.timegm(time.time_struct or the tuple in utc) \
-> seconds since epoch]" )
# calendar.timegm(time.struct_time or the tuple in utc) -> seconds since epoch
import calendar
print(calendar.timegm((1970, 1, 1, 0, 0, 0, 3, 1, 0)))
print(calendar.timegm(time.gmtime(0)))

print("[ # 2: time.mktime(time.struct_time in utc) - time.timezone ]")
# time.mktime(time.struct_time or the tuple in utc) - time.timezone
print(f"time.timezone = {time.timezone}")
print(type(time.timezone))
print(time.mktime(time.gmtime(time.time())) - time.timezone)
print(time.time())


print("\n[ time.asctime(time.struct_time or the tuple) -> str ]")
print(time.asctime(time.gmtime(0)))


print("\n[ time.strftime(a format, time.struct_time or the tuple) \
-> str based on the format ]")
# some directive like weekday name in the format is affected by locale
import locale
print(locale.getlocale())

print(time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime(time.time())))


print("\n[ time.strptime(string of time, the format of the string) \
-> time.struct_time ]")
print(time.strptime("1970-01-01 00:00:00 Wednesday", \
    "%Y-%m-%d %H:%M:%S %A"))