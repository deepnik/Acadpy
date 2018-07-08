#Insert values in the tables.
import sqlite3

db=sqlite3.connect("data.db")
cursor=db.cursor()
cursor.execute("insert into book values(002,'Science','India','Theory')")
cursor.execute("insert into titles values(002,'FOX','1101',110,2010)")
cursor.execute("insert into publisher values(002,'ABC','India',10102,11101)")
cursor.execute("insert into zip_code values(002,'Mullana','Haryana',134003)")
cursor.execute("insert into author_title values(002,11010,1010012)")
cursor.execute("insert into author values(002,'Chris','Lynn','White')")
db.commit()
db.close()
