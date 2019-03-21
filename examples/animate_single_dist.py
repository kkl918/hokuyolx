#!/usr/bin/python3
'''Animates distances using single measurment mode'''
from hokuyolx import HokuyoLX
import matplotlib.pyplot as plt
import datetime 


DMAX = 10000

def update(laser, plot, text, log):
    timestamp, scan = laser.get_filtered_dist(dmax=DMAX)
    
    plot.set_data(*scan.T)
    text.set_text('t: %d' % timestamp)
    plt.draw()
    plt.pause(0.001)

def run():
    log = open("./log_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),'a')
    plt.ion()
    laser = HokuyoLX()
    ax = plt.subplot(111, projection='polar')
    plot = ax.plot([], [], '.')[0]
    text = plt.text(0, 1, '', transform=ax.transAxes)
    ax.set_rmax(DMAX)
    ax.grid(True)
    plt.show()
    while plt.get_fignums():
        update(laser, plot, text,f)
        # log version 1
        #ts, sc = laser.get_filtered_dist(dmax=DMAX)
        #for i in sc:
        #    print(str(ts)+','+str(i[0])+','+str(i[1]))
        #    f.write(str(ts) + ',' + str(i[0]) + ',' + str(i[1]) + '\n')
    laser.close()

if __name__ == '__main__':
		run()
