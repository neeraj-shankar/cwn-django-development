from datetime import datetime

now = datetime.now()
uniqueID = now.strftime('%y%m%d%H%M%S')
print('Using Unique ID:', uniqueID)