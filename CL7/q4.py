#Extract day from the time.


from datetime import datetime

now=datetime.now()

print("day:",now.strftime("%A"))
