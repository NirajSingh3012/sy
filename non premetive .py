# Define processes with their names, arrival times, and burst times
processes = [
    {"name": "P1", "arrival_time": 0, "burst_time": 10},
    {"name": "P2", "arrival_time": 2, "burst_time": 5},
    {"name": "P3", "arrival_time": 4, "burst_time": 8},
    {"name": "P4", "arrival_time": 6, "burst_time": 3}
]

# Initialize variables
current_time = 0
total_waiting_time = 0

print("Process\tStart Time\tEnd Time\tWaiting Time")

# Loop through each process
for process in processes:
    # Calculate waiting time
    waiting_time = max(0, current_time - process["arrival_time"])
    total_waiting_time += waiting_time

    # Update current time
    current_time += process["burst_time"]

    # Print process execution details
    print(f"{process['name']}\t{max(current_time - process['burst_time'], process['arrival_time'])}\t\t{current_time}\t\t{waiting_time}")

# Calculate average waiting time
average_waiting_time = total_waiting_time / len(processes)
print("\nAverage Waiting Time:", average_waiting_time)
