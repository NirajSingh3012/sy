def fcfs_scheduling(processes):
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for process in processes:
        if current_time < process[0]:
            current_time = process[0]

        waiting_time = current_time - process[0]
        turnaround_time = waiting_time + process[1]

        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        current_time += process[1]

    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)

    return average_waiting_time, average_turnaround_time

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append((arrival_time, burst_time))

    avg_waiting_time, avg_turnaround_time = fcfs_scheduling(processes)

    print("\nAverage Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)
