n = int(input("Enter the number of processes:   "))

quantum = int(input("Enter the time quantum"))

time=0
processes =[]
wait_time = []
tat = []

total_time =0


for i in range(n):
    print("Enter the arrival time and the burst time ", i+1)

    inp = list(map(int, input().split()))


    #inp = [0,10]

    AT,BT,RT =inp[0],inp[1], inp[1]

    processes.append([AT,BT,RT,0])


    total_time += BT

while(total_time>0):
    for i in range(len(processes)):
        

