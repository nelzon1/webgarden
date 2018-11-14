import camera
import time

while True:
    now = time.localtime()
    timestr = str(now[1]) + '/' + str(now[2]) + '/' + str(now[0]) + ' - ' + str(now[3]) + ':' + str(now[4])
    timestamp = now[0] + now[1] + now[2] + now[3] + now[4]
    camera.snap('images/' + timestamp + '.jpg', timestr)
    time.sleep(300)
