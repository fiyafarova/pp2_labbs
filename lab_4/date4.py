from datetime import datetime

date1 = datetime(2025, 2, 21, 12, 0, 0)  #Feb 21, 2025, 12:00 
date2 = datetime(2025, 2, 18, 8, 30, 0)  #Feb 18, 2025, 8:30 

difference = abs((date1 - date2).total_seconds())

print(f"Difference between the two dates in seconds: {difference} seconds")
