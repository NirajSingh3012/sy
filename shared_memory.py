import random
import time
import threading

lock=threading.Lock()
count=0
buffer=[]

def producer():
    global lock,count,buffer
    for i in range(10):
        num = random.randint(0,100)
        print(f"Items Produced : {num}")
        lock.acquire()
        buffer.append(num)
        lock.release()
        count=count+1
        time.sleep(random.randint(1,2))

def consumer():
    while (True):
        if len(buffer)==0 and count==10:
            break
        if not buffer:
            continue
        lock.acquire()
        print(f"Items Consumed : {buffer.pop(0)}")
        lock.release()
        time.sleep(random.randint(2,3))

t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()


    
