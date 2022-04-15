# 很容易写出转移方程。动态规划求解
n,m = input().split()
n,m = int(n),int(m)
dataMap = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    s = input().split()
    for j in range(m):
        dataMap[i][j] = int(s[j])
result = [[float('-inf') for i in range(m)]for j in range(n)]
result[0][0] = dataMap[0][0]
for i in range(1,n):
    i1 = i-3
    if(i1<0):i1=0
    for ii in range(i1,i):
        if(result[ii][0]+dataMap[i][0]>result[i][0]):
            result[i][0] = result[ii][0]+dataMap[i][0]

for j in range(1,m):
    j1 = j-3
    if(j1<0):j1=0
    for jj in range(j1,j):
        if(result[0][jj]+dataMap[0][j]>result[0][j]):
            result[0][j] = result[0][jj]+dataMap[0][j]

for i in range(1,n):
    for j in range(1,m):
        i1 = i-3
        if(i1<0):i1=0
        for ii in range(i1,i):
            if(result[ii][j]+dataMap[i][j]>result[i][j]):
                result[i][j] = result[ii][j]+dataMap[i][j]
        j1 = j-3
        if(j1<0):j1=0
        for jj in range(j1,j):
            if(result[i][jj]+dataMap[i][j]>result[i][j]):
                result[i][j] = result[i][jj]+dataMap[i][j]

print(result[n-1][m-1])