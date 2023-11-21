import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

# creating a datetime object
date_of_birth = dt.datetime(year=2002, month=1, day=8, hour=7)
print(date_of_birth)