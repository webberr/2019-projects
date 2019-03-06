import time 
from datetime import date 

today = date.today()
deadline = date(today.year, 5, 24)

if deadline > today:
    print(deadline - today)



