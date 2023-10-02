import threading
import time
def print_num():
    for i in range(1,6):
        print(i)

def main():
    t1=threading.Thread(target=print_num)
    t1.start()
    t1.join()
    time.sleep(2)

main()
