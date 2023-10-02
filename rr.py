def rr(processes,burst_time,time_quantum):
    n=len(processes)
    remaining_time=burst_time.copy()
    time=0
    while any(remaining_time):
        for i in range(n):
            if remaining_time[i]>0:
                if remaining_time[i]>time_quantum:
                    time+=time_quantum
                    remaining_time[i]-=time_quantum
                else:
                    time+=remaining_time[i]
                    remaining_time[i]=0
                    print(f"Process {processes[i]} executed in {time}")


if __name__ == "__main__":
    processes=["p1","p2","p3","p4"]
    burst_time=[10,5,8,12]
    time_quantum = 3
    print(rr(processes,burst_time,time_quantum))


