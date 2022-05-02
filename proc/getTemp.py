import temperature as temp
import time
import os
import json
import sqlite3

dbconn = sqlite3.connect('/home/piserver/dev/webgarden/appDB.sqlite3')
mycursor = dbconn.cursor()

def writeTemp(tempData, timeStr):
    sql = "INSERT INTO Temperature (Temperature,Datetime) VALUES (?,'?')"
    val = (tempData,timeStr)
    mycursor.execute(sql,val)

now = time.localtime()
timeStr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
datestamp = str(now[0]) +  '-' + str(now[1]).zfill(2) +  '-' + str(now[2]).zfill(2)
curTemp = temp.read_temp()[0]
#import pdb; pdb.set_trace()
print("Current temperature: ", curTemp, timeStr)
writeTemp(curTemp, timeStr)
dbconn.close()

