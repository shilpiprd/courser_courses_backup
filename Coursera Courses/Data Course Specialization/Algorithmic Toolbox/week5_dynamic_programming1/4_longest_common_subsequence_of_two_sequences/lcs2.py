#longest common subsequence for 2 strings: works perfectly
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

value = lcs(l1,l2)
print(value)

