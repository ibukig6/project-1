import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE Users (id primarykey auto_increment, name nvarchar(20), account nvarchar(40), password nvarchar(40))')
print ("Table created successfully")
conn.close()