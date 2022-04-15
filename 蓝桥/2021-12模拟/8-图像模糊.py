'''
编程题

小蓝有一张黑白图像，由n*m个像素组成，其中从上到下共n行，每行从左到右m列。
每个像素由一个0到255之间的灰度值表示。

现在，小蓝准备对图像进行模糊操作，操作的方法为：

对于每个像素，将以它为中心3*3区域内的所有像素（可能是9个像素或少于9个像素）
求和后除以这个范围内的像素个数（取下整），得到的值就是模糊后的结果。

请注意每个像素都要用原图中的灰度值计算求和。
【输入格式】

输入的第一行包含两个整数n,m。

第2行到第n+1行每行包含m个整数，表示每个像素的灰度值，相邻整数之间用一个空格分隔。

【输出格式】

输出n行，每行m个整数，相邻整数之间用空格分隔，表示模糊后的图像。
【样例输入】

3 4

0 0 0 255

0 0 255 0

0 30 255 255

【样例输出】

0 42 85 127

5 60 116 170

7 90 132 191
'''

n,m = (input().split())
n,m = int(n),int(m)
data = [[0 for i in range(m)] for j in range(n)]
data2 = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    s = input().split(' ')
    for j in range(m):
        data[i][j] = int(s[j])

for i in range(n):
    for j in range(m):
        i1 = i-1
        i2 = i+1
        j1 = j-1
        j2 = j+1
        if(i1<0):i1 = 0
        if(j1<0):j1 = 0
        if(j2>=m):j2 = m-1
        if(i2>=n):i2 = n-1
        sum = 0
        for ii in range(i1,i2+1):
            for jj in range(j1,j2+1):
                sum += data[ii][jj]
        data2[i][j] = sum//((i2-i1+1)*(j2-j1+1))

for i in range(n):
    for j in range(m):
        print(data2[i][j],end=' ')
    print()