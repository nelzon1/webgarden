import camera
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

def writeImagePath(image_path, timeStr):
    sql = "INSERT INTO images VALUES (%s,%s)"
    val = (image_path,timeStr)
    mycursor.execute(sql,val)
    mycursor.commit()

while True:
    now = time.localtime()
    timeStr = str(now[1]) + '/' + str(now[2]) + '/' + str(now[0]) + ' - ' + str(now[3]) + ':' + str(now[4])
    timestamp = str(now[0]) + str(now[1]).zfill(2) + str(now[2]).zfill(2) + str(now[3]).zfill(2) + str(now[4]).zfill(2)
    datestamp = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    image_path = os.path.join("..","dash","static","dash","images", datestamp ,timestamp + '.jpg')
    camera.snap(image_path, timeStr)
    writeImagePath(image_path, timeStr)
    time.sleep(300)
