import random
import threading
import queue
import time

queue=queue.Queue(10)

def producer():
    for i in range(0,x):
        num=random.randint(1,100)
        print(f"Producer produced :{num}")
        queue.put(num)
        time.sleep(random.randint(1,2))

def consumer():
    for i in range(0,x):
    #while(true):
        num=queue.get()
        queue.task_done()
        print(f"Consumer Consumed : {num}")
        time.sleep(random.randint(2,5))

x=int(input("Enter No Times Items To Be Produced :"))
t1=threading.Thread(target=producer)
t2=threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
queue.get()

#if __name__ == "__main__":
        
        
              
