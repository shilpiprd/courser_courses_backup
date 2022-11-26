#the goldbag problem
W,n = map(int,input().split())
wt = list(map(int,input().split()))
val = wt
          
def knapsack(W, wt, val):

    T = [[None]*(len(wt)+1) for _ in range(W+1)]
    for u in range(W+1):
        T[u][0] = 0
    for k in range(1,len(wt)+1):
        T[0][k] = 0

    for i in range(1,len(wt)+1):
        for u in range(W+1):
            T[u][i] = T[u][i-1]
            if u >= wt[i-1]:
                T[u][i] = max(T[u][i], T[u-wt[i-1]][i-1]+val[i-1])
                
    return T[u][i]    
          
print(knapsack(W,wt,val))
