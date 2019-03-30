#!/usr/bin/python3
'''Animates distances using single measurment mode'''
from hokuyolx import HokuyoLX
import matplotlib.pyplot as plt
import datetime

DMAX = 10000
IMIN = 300.
IMAX = 2000.

def get_colors(intens):
    max_val = intens.max()
    return np.repeat(intens, 3).reshape((4,3))/max_val 

def update(laser, plot, text, log):
    timestamp, scan = laser.get_filtered_intens(dmax=DMAX)
    
    # varible "scan" return array with measured angles, distances and intensities
    #   0          1           2
    # angle    distance   intensities
    log.write(str(timestamp)+',')
    
    for distance    in scan[:,1]:        # write distance
        log.write(str(distance)+',')
    for intensities in scan[:,2]:        # write intensities
        log.write(str(intensities)+',')    
    log.write('\n')                      # chahge line   
    
    print(timestamp,len(scan[:,1]),len(scan[:,2]),scan[:,1][540],scan[:,2][540])
    plot.set_offsets(scan[:, :2])        # row all ,0-2 col 
    plot.set_array(scan[:, 2])           # row all ,2   col 
    text.set_text('t: %d' % timestamp)
    plt.show()
    plt.pause(0.001)

def run():
    log = open("./log_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),'a')
    plt.ion()
    laser = HokuyoLX()
    ax = plt.subplot(111, projection='polar')
    plot = ax.scatter([0, 1], [0, 1], s=5, c=[IMIN, IMAX], cmap=plt.cm.Greys_r, lw=0)
    text = plt.text(0, 1, '', transform=ax.transAxes)
    ax.set_rmax(DMAX)
    ax.grid(True)
    plt.show()
    while plt.get_fignums():
        update(laser, plot, text, log)
    laser.close()

if __name__ == '__main__':
    run()
