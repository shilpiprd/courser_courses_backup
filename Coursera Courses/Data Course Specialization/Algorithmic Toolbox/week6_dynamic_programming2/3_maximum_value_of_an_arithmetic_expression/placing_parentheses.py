from numpy import inf
def para(array):
    op = []
    n = int((len(array) +1)/2)
    m = [[0]*(n) for _ in range(n)]
    M = [[0]*(n) for _ in range(n)]
    number =['0','1','2','3','4','5','6','7','8','9']
    c = 0
    for i in array:
        if i in number:
            m[c][c] = int(i)
            M[c][c] = int(i)
            c+=1
        else:
            op.append(i)
        #else list.append(op) #a list of opeartors
    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s
            m[i][j],M[i][j] = MinAndMax(i,j,m,M,op) #filling the table
            
    return M[0][n-1]

def MinAndMax(i,j,m,M,op): #i and j are indices and m and M are tables
    minima = float(inf)
    maxima = -float(inf)
    for k in range(i,j):
        if op[k] == '*':
            a = M[i][k] * M[k+1][j]
            b = M[i][k] * m[k+1][j]
            c = m[i][k] * M[k+1][j]
            d = m[i][k] * m[k+1][j]
        elif op[k] == '+':
            a = M[i][k] + M[k+1][j]
            b = M[i][k] + m[k+1][j]
            c =m[i][k]+ M[k+1][j]
            d =m[i][k] + m[k+1][j]   
        else:
            a = M[i][k] - M[k+1][j]
            b = M[i][k] - m[k+1][j]
            c =m[i][k]- M[k+1][j]
            d =m[i][k] - m[k+1][j]
        minima = min(minima,a,b,c,d)
        maxima = max(maxima,a,b,c,d)
    return (minima,maxima)

print(para(list(input())))
