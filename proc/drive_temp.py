import temperature as temp:
import time

while True:
    now = time.localtime()
    timestr = now[0] + '-' + now[1] + '-' + now[2] + ' ' + now[3] + ':' + now[4]
    datestamp = now[0] + '-' + now[1] + '-' + now[2]
    curTemp = temp.read_temp()
    try:
        with open(datestamp + '.dat','a') as data:
            data.write(curTemp[0] + ',' + curTemp[1] + ',' + timestr + '\n')
    except:
        print('File write error')
    time.sleep(15)
