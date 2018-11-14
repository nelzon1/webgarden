import temperature as temp
import time
import os

while True:
    now = time.localtime()
    timestr = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2) + ' ' + str(now[3]).zfill(2) + ':' + str(now[4]).zfill(2) + ':' + str(now[5]).zfill(2)
    datestamp = str(now[0]) + '-' + str(now[1]).zfill(2) + '-' + str(now[2]).zfill(2)
    curTemp = temp.read_temp()
    #import pdb; pdb.set_trace()
    try:
        with open(os.path.join("tempdata", datestamp + '.dat'),'a') as data:
            datum = (str(curTemp[0]) + ',' + str(curTemp[1]) + ',' + timestr + '\n')
            print(datum[:-1])
    except:
        print('File write error')
    time.sleep(60)
