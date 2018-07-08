#Update any values in any of the tables. Print the original and updated values.

import sqlite3

db=sqlite3.connect("data.db")
cursor=db.cursor()
cursor.execute("update book set gener='Technology' where book_id=001")

db.commit()
db.close()
