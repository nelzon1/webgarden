import sqlite3

dbconn = sqlite3.connect('/home/piserver/dev/webgarden/appDB.sqlite3')
cur = dbconn.cursor()

count = list(cur.execute("SELECT COUNT(1) FROM Temperature"))

latest = list(cur.execute("select * from temperature"))

print("Count: ", count)
print("Latest: ", latest)
