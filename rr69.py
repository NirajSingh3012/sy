def rr(processes,bt,tq):
    time=0
    n=len(processes)
    rt=bt.copy()
    while any (rt):
        for i in range(n):
            if rt[i]>0:
                if rt[i]>tq:
                    time+=tq
                    rt[i]-=tq
                else:
                    time+=rt[i]
                    rt[i]=0
                    print(f"process {processes [i]} executed in time : {time}")

if __name__ == "__main__":
    tq=3
    processes=["p1","p2","p3","p4"]
    bt=[10,5,8,12]
    print(rr(processes,bt,tq))
