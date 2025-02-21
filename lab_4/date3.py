import datetime

timenow = datetime.datetime.now() 

print(timenow.replace(microsecond=0))
