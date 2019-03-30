#!/usr/bin/python3
from hokuyolx import HokuyoLX
import time, datetime, threading
import threading
import time
from queue import Queue

now = time.time()
future = now + 11

DMAX = 10000
IMIN = 300.
IMAX = 2000.
laser = HokuyoLX()

def thread_job():
    timestamp, scan = laser.get_filtered_intens(dmax=DMAX) 
    q.put(timestamp) # 將結果放進 queue
    # return arr # 上面這一步驟取代了 return

def multithreading():
    q = Queue()   # 宣告 Queue 物件
    threads = []  # 用來放 thread 的 array
    for i in range(4):
        t = threading.Thread(target=thread_job) # 將 data 與 queue 傳入 thread 裡面
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join() # 每個 thread 都要做 join

    results = [] # 用來接收與顯示結果的 array

    for _ in range(4):
        results.append(q.get()) # 取出 queue 裡面的資料
    print(results) # 顯示執行後的結果

if __name__=='__main__':
    multithreading()