#Extract month from the time.

from datetime import datetime

now=datetime.now()

print("month:",now.strftime("%B"))

