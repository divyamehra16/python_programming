# datetime - module
"""
datetime.now() --> current date
date.today()   --> today's date
time.delta(days=<value>)  --> represent the difference
strftime(format)        --> date/time to string type conversion
strptime(string,format)        --> string to date/time conversion
"""

import datetime
now=datetime.datetime.now()
print(now)
formatted=now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)