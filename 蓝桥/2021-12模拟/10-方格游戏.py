'''
小蓝在一个n行m列的方格图中玩一个游戏。

开始时，小蓝站在方格图的左上角，即第1行第1列。

小蓝可以在方格图上走动，走动时，如果当前在第r行第c列，他不能走到行号比r小的行，也不能走到列号比c小的列。
同时，他一步走的直线距离不超过3.

例如，如果当前小蓝在第3行第5列，他下一步可以走到第3行第6列、第3行第7列、第3行第8列、第4行第5列、
第4行第6列、第4行第7列、第5行第5列、第5行第6列、第6行第5列之一。

小蓝最终要走到第n行第m列。

在图中，有的位置有奖励，走上去即可获得，有的位置有惩罚，走上去就要接受惩罚。奖励和惩罚最终抽象成一个权值，
奖励为正，惩罚为负。

小蓝希望，从第1行第1列走到第n行第m列后，总的权值和最大。请问最大是多少？
【输入格式】

输入的第一行包含两个整数n,m，表示图的大小。

接下来n行，每行m个整数，表示方格图中每个点的权值。

【输出格式】

输出一个整数，表示最大权值和。
【样例输入】

3 5
-4 -5 -10 -3 1
7 5 -9 3 -10
10 -2 6 -10 -4

【样例输出】

15
'''
# 最短路径求解。每个点至于条件之内的点有一条有向边
n,m = input().split()
n,m = int(n),int(m)
dataMap = [[0 for i in range(m)]for j in range(n)]
for i in range(n):
    s = input().split()
    for j in range(m):
        dataMap[i][j] = int(s[j])

result = [[float('-inf') for i in range(m)]for j in range(n)]
result[0][0] = dataMap[0][0]
road = {(0,0)}#最开始的点
while(len(road)!=0):
    (i,j) = road.pop()
    im = i+3
    if(im>=n):im = n-1
    jm = j+3
    if(jm>=m):jm = m-1
    for ii in range(i+1,im+1):
        road.add((ii,j))
        if(result[i][j]+dataMap[ii][j]>result[ii][j]):
            result[ii][j] = result[i][j]+dataMap[ii][j]
    for jj in range(j+1,jm+1):
        road.add((i,jj))
        if(result[i][j]+dataMap[i][jj]>result[i][jj]):
            result[i][jj] = result[i][j]+dataMap[i][jj]

print(result[n-1][m-1])