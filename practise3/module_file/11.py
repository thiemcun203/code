import datetime
def add_days(cur_date, n):
    return cur_date+ datetime.timedelta(days=n)
# (timedelta plus and auto give exactly day)