import camera
import time
import os

import json

creds = {}
with (open('dbinfo.json','r') as options):
    creds = json.loads(options)

dbconn = sqlite3.connect(creds['dbPath'])
dbcurr = dbconn.cursor()

def writeImagePath(image_path, timeStr):
    sql = "INSERT INTO images (path,datetime) VALUES (%s,%s)"
    val = (image_path,timeStr)
    dbcurr.execute(sql,val)
    dbconn.commit()

while True:
    now = time.localtime()
    timeStr = str(now[1]) + '/' + str(now[2]) + '/' + str(now[0]) + ' - ' + str(now[3]) + ':' + str(now[4])
    timestamp = str(now[0]) + str(now[1]).zfill(2) + str(now[2]).zfill(2) + str(now[3]).zfill(2) + str(now[4]).zfill(2)
    datestamp = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    dateTime = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
    image_path = os.path.join("..","dash","static","dash","images", datestamp ,timestamp + '.jpg')
    camera.snap(image_path, timeStr)
    writeImagePath(image_path, dateTime)
    time.sleep(300)
