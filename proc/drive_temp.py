import temperature as temp
import time
import os
import json
import sqlite3

creds = {}
with (open('dbinfo.json','r') as options):
    creds = json.loads(options)

dbconn = sqlite3.connect(creds['dbPath'])
mycursor = dbconn.cursor()

def writeTemp(tempData, timeStr):
    sql = "INSERT INTO temperature (temperature,datetime) VALUES (?,?)"
    val = (tempData,timeStr)
    mycursor.execute(sql,val)
    mydb.commit()

while True:
    now = time.localtime()
    timeStr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
    datestamp = str(now[0]) +  '-' + str(now[1]).zfill(2) +  '-' + str(now[2]).zfill(2)
    curTemp = temp.read_temp()[0]
    #import pdb; pdb.set_trace()
    writeTemp(curTemp, timeStr)
    try:
        
        """
        with open(os.path.join("tempdata", datestamp + '.dat'),'a') as data:
            datum = (str(curTemp[0]) + ',' + str(curTemp[1]) + ',' + timestr + '\n')
            data.write(datum)
            print(datum[:-1])
        """
    except:
        print('Database write error')
    time.sleep(60)

dbconn.close()