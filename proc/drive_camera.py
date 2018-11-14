import camera
import time
import os

while True:
    now = time.localtime()
    timestr = str(now[1]) + '/' + str(now[2]) + '/' + str(now[0]) + ' - ' + str(now[3]) + ':' + str(now[4])
    timestamp = str(now[0]) + str(now[1]).zfill(2) + str(now[2]).zfill(2) + str(now[3]).zfill(2) + str(now[4]).zfill(2)
    datestamp = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    camera.snap(os.path.join("..","dash","static","dash","images", datestamp ,timestamp + '.jpg'), timestr)
    time.sleep(300)
