#### primitive Calculator : obvious answer : this should probably work
# n = int(input())
n = int(input())
count = 0
arr = []
while n!=1:
    if n %3 == 0:
        arr.append(n)
        if n//3 !=0:
            n = n//3
        else:
            n = 1
        # arr.append(n)
        count +=1
    elif (n-1) % 3 == 0:
        arr.append(n)
        if (n-1) !=0:
            n -=1
        else:
            n = 1
        
        # arr.append(n)
        count +=1 
    elif (n %2) == 0:
        arr.append(n)
        if (n // 2) !=0:
            n = n//2
        else:
            n = 1
        # arr.append(n)
        count += 1
    else:
        arr.append(n)
        if (n-1) != 0:
            n -=1
        # arr.append(n)
        count +=1
arr.append(1)
print(count)
print(*arr)
