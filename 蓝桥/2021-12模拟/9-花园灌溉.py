'''
小蓝负责花园的灌溉工作。

花园可以看成一个n行m列的方格图形。中间有一部分位置上安装有出水管。

小蓝可以控制一个按钮同时打开所有的出水管，打开时，有出水管的位置可以被认为已经灌溉好。

每经过一分钟，水就会向四面扩展一个方格，被扩展到的方格可以被认为已经灌溉好。
即如果前一分钟某一个方格被灌溉好，则下一分钟它上下左右的四个方格也被灌溉好。

给定花园水管的位置，请问k分钟后，有多少个方格被灌溉好？
【输入格式】

输入的第一行包含两个整数n,m。

第二行包含一个整数t，表示出水管的数量。

接下来t行描述出水管的位置，其中第i行包含两个数r,c表示第r行第c列有一个排水管。

接下来一行包含一个整数k。

【输出格式】
【样例输入】

3 6

2

2 2

3 4

1

【样例输出】

9
输出一个整数，表示答案。
'''
n,m = input().split()
n,m = int(n),int(m)
data = [[0 for i in range(m)]for j in range(n)]
location = []
t = int(input())
for i in range(t):
    r,c = input().split()
    r,c = int(r),int(c)
    location.append((r-1,c-1))
    data[r-1][c-1] = 1
k = int(input())

for (i,j) in location:
    i1 = i-k
    i2 = i+k
    j1 = j-k
    j2 = j+k
    if(i1<0):i1=0
    if(i2>=n):i2=n-1
    if(j1<0):j1=0
    if(j2>m):j2=m-1
    for ii in range(i1,i2+1):
        data[ii][j] = 1
    for jj in range(j1,j2+1):
        data[i][jj] = 1

re = 0
for i in range(n):
    for j in range(m):
        if(data[i][j]==1):
            re+=1

print(re)