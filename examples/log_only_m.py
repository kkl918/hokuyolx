#!/usr/bin/python3
'''Animates distances using single measurment mode'''
from hokuyolx import HokuyoLX
import time, datetime, threading
from queue import Queue


now = time.time()
future = now + 2

DMAX = 10000
IMIN = 300.
IMAX = 2000.
laser = HokuyoLX()

log = open("/media/linaro/50EC-88F2/log_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),'a')   
    
result = []

if __name__ == '__main__':
    while time.time() < future: 
        
        timestamp, scan = laser.get_filtered_intens(dmax=DMAX) 
        s = str(timestamp)+','
        
        
        #log_now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        #log.write(str(timestamp)+',')
        
        for distance    in scan[:,1]:        # write distance
            #log.write(str(distance)+',')
            s = s + str(distance)+','
        for intensities in scan[:,2]:        # write intensities
            s = s + str(intensities)+','    
        s = s + '\n'
        result.append(s)
        #log.write('\n')    

    
    laser.close()
    
    for i in result:
        log.write(i)
    log.close()
    print('Done!!')