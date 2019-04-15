import temperature as temp
import time
import os
import json
import mysql.connector

global cred

with open('dbinfo.json','r') as json_file:
    cred = json.load(json_file)

mydb = mysql.connector.connect(
        host=cred['connection']['host'],
        user=cred['connection']['user'],
        passwd=cred['connection']['pwd'],
        database=cred['connection']['database'],
        #port=cred['connection']['port']
        )

mycursor = mydb.cursor()

def writeTemp(tempData, timeStr):
    sql = "INSERT INTO temperature VALUES (%s,%s)"
    val = (tempData,timeStr)
    mycursor.execute(sql,val)
    mycursor.commit()

while True:
    now = time.localtime()
    timeStr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
    datestamp = str(now[0]) +  '-' + str(now[1]).zfill(2) +  '-' + str(now[2]).zfill(2)
    curTemp = temp.read_temp()
    #import pdb; pdb.set_trace()
    try:
        writeTemp(curTemp, timeStr)
        """
        with open(os.path.join("tempdata", datestamp + '.dat'),'a') as data:
            datum = (str(curTemp[0]) + ',' + str(curTemp[1]) + ',' + timestr + '\n')
            data.write(datum)
            print(datum[:-1])
        """
    except:
        print('Database write error')
    time.sleep(60)
