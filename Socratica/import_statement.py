
import math
import datetime

print(dir(datetime))

# print(dir(math))
#
# help(math.radians)

gvr = datetime.date(1956, 1, 31)

print(gvr)

print(gvr.day)
print(gvr.month)
print(gvr.year)

mil = datetime.date(2000,1,1)

dt = datetime.timedelta(100)

print(mil + dt)

print(mil)
