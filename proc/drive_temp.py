import temperature as temp
import time

while True:
    now = time.localtime()
    timestr = str(now[0]) + '-' + str(now[1]) + '-' + str(now[2]) + ' ' + str(now[3]) + ':' + str(now[4])
    datestamp = str(now[0]) + '-' + str(now[1]) + '-' + str(now[2])
    curTemp = temp.read_temp()
    try:
        with open(datestamp + '.dat','a') as data:
            data.write(curTemp[0] + ',' + curTemp[1] + ',' + timestr + '\n')
    except:
        print('File write error')
    time.sleep(15)
