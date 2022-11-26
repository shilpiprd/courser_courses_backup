#trying for the 3nd time: Network packet processing simulation
s,n = map(int,input().split())
temps = s
buffer = [] #empty buffer of presumably size s   
diff = [] #to measure the time difference between 2 incoming packets
count = 0 
start_time = 0
count_list = []
for i in range(n):
    ai,pi = map(int,input().split())
    if i==0:
        start_time = ai
        diff.append(start_time)
        buffer.append(ai+pi)
        count_list.append(count)
        count += ai +pi
        temps-=1
        continue
    if(temps>0):
        if(ai-count>0):
            buffer.append(pi+ (ai-count))
            diff.append(ai-count)
            count_list.append(count)
            count+= pi + (ai-count)
        else:
            buffer.append(pi)
            diff.append(0)
            count_list.append(count)
            count += pi
        temps-=1
    elif (temps==0): #check if 
        if(ai>=count):
            buffer.append(pi+(ai-count))
            diff.append(ai-count)
            count_list.append(count)
            count += pi + (ai-count)
        else:
        #check finally if even one item can leave before completely rejecting.
            if (s> 1) and (ai>=count_list[i-s]+buffer[(i-s)+1]):
                buffer.append(pi) #no way ai>count...
                diff.append(0)
                continue
            diff.append(0)
            buffer.append(-1)

count = 0
for i in range(len(buffer)):
    if i==0:
        print(start_time)
        count += buffer[0]
    elif (buffer[i] == -1):
        print(-1)
        continue
    else:
        print(count+diff[i])
        count += buffer[i]
