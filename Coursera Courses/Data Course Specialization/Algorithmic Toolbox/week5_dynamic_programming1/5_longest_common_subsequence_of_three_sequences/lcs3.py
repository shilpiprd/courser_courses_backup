#finding a solution to comparet three strings
def lcs(l1,l2):
    t = [[0]*(len(l1)+1) for i in range(len(l2)+1)]
    for j in range(1,len(l2)+1):
        for i in range(1,len(l1)+1):
            if l1[i-1] == l2[j-1]:
                t[j][i] = t[j-1][i-1] +1
            else:
                t[j][i] = max(t[j-1][i],t[j][i-1])
    return t[j][i]


n1 = int(input())
l1 = list(map(int,input().split()))
n2 = int(input())
l2 = list(map(int,input().split()))  
n3 = int(input())
l3 = list(map(int,input().split()))  

a = lcs(l1,l2)
b = lcs(l2,l3)
c = lcs(l3,l1)

if (a==b) and (b==c):
    print(a) 
elif a==b and a !=c:
    if a<=c:
        print(a)
    else:
        print(c)
elif a == c and a!=b:
    if a <= b:
        print(a)
    else:
        print(b)
elif b == c and b != a:
    if b<=a :
        print(b)
    else:
        print(a)
elif a!= b and b !=c:
    print(min(a,b,c))
