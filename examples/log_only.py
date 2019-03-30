#!/usr/bin/python3
from hokuyolx import HokuyoLX
import time, datetime

now = time.time()
future = now + 11

DMAX = 10000
IMIN = 300.
IMAX = 2000.
laser = HokuyoLX()

log = open("/media/linaro/50EC-88F2/log_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),'a')   
    
result = 0

if __name__ == '__main__':
    while time.time() < future:       
        ts, scan = laser.get_dist()
        for i in scan:
            log.write(i)
        # timestamp, scan = laser.get_dist()
        #log_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # log.write(str(timestamp)+',')

        # for distance    in scan[:,1]:        # write distance
            # log.write(str(distance)+',')

        # for intensities in scan[:,2]:        # write intensities
            # log.write(str(intensities)+',')
        
        # log.write('\n')   
        # result = result +1
    
    laser.close()
    log.close()
    print('Done:',result)