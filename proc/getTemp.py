import temperature as temp
import time
import os
import sqlite3


creds = {}
with (open('dbinfo.json','r') as options):
    creds = json.loads(options)

dbconn = sqlite3.connect(creds['dbPath'])
dbcurr = dbconn.cursor()

def writeTemp(tempData, timeStr):
    sql = "INSERT INTO Temperature (Temperature,Datetime) VALUES (?,?)"
    val = (tempData,timeStr)
    dbcurr.execute(sql,val)

now = time.localtime()
timeStr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
datestamp = str(now[0]) +  '-' + str(now[1]).zfill(2) +  '-' + str(now[2]).zfill(2)
curTemp = temp.read_temp()[0]
#import pdb; pdb.set_trace()
print("Current temperature: ", curTemp, timeStr)
writeTemp(curTemp, timeStr)
dbconn.commit()
dbconn.close()

