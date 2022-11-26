from numpy import inf
from math import sqrt
n = int(input())
d = list()
same = False
for i in range(n):
    key,value = map(float,input().split())
    if (key,value) in d:
        dmin = 0
        dis = 0
        same = True
        break
    else:
        d.append((key,value))

if n ==2 and same == False:

    dmin = sqrt((abs(d[0][0]) - abs(d[1][0]))** 2 + (abs(d[0][1]) - abs(d[1][1]) ) ** 2) 
    dis = dmin
    
elif n!=2 and same==False:
    
    d = sorted(d, key=lambda x: x[0]) #code to sort based on x coordinates
    sub1 = d[ :n//2]
    sub2 = d[n//2:]

    dl = float(inf)
    for i in range(len(sub1)-1):
        distance = sqrt((abs(sub1[i][0]) - abs(sub1[i+1][0])** 2+ (abs(sub1[i][1]) - abs(sub1[i+1][1])))** 2) 
        if distance < dl:
            dl = distance #d1 should be minimum
            
    dr =float(inf)
    for i in range(len(sub2)-1):
        distance = sqrt((abs(sub2[i][0]) - abs(sub2[i+1][0])) ** 2+ (abs(sub2[i][1]) - abs(sub2[i+1][1]) )** 2) 
        if distance<dr:
            dr = distance
    dmin = min(dl,dr)

    x = abs(d[int(n//2)][0])
    strip  =[]
    for i in d:
        diff = abs(i[0]) - x
        if int(diff) < (abs(dmin)):
            strip.append(i)
    # print(strip is created)
    #now sort strip on the basis of y coordinates
    stripf = sorted(strip, key=lambda i: i[1]) #final strip sorted on y coords
    dis = float(inf)
    for i in range(len(stripf) - 1):
        for j in range(i+1,i+8): #for every point consider next 7 points
            try:
                val=sqrt((abs(stripf[i][0])-abs(stripf[j][0])**2+(abs(stripf[i][1])-abs(stripf[j][1]) )** 2))
                if float(val) < dis:
                    dis = val
            except:
                break
print(format(min(dis,dmin),".9f"))

