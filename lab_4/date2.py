import datetime

timenow = datetime.datetime.now() 

delta = datetime.timedelta(days=1)

print(f" YESTERDAY:{timenow-delta}\n TODAY:{timenow}\n TOMORROW:{timenow+delta}")
