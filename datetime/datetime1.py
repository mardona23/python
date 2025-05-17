import datetime
from datetime import date
t=date.today()
print(t)
x=datetime.datetime.now()
print(x)
a=datetime.datetime(2014,9,3,3,39,56)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
import calendar
yy=2084
mm=2
print(calendar.month(yy,mm))
print(t.strftime("%m/%d/%Y"))