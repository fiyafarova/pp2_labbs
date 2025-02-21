import datetime

timenow = datetime.datetime.now() 

delta = datetime.timedelta(days=5)
new_date = timenow - delta
print(new_date)
