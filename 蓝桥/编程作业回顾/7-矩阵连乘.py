s = input().split()
p = []
for i in s:
    p.append(int(i))
n = len(p)-1
m = [[0 for i in range(n)]for j in range(n)]
s = [[0 for i in range(n)]for j in range(n)]

for len in range(1,n):
    for i in range(n-len):
        j = i+len
        m[i][j] = float('inf')
        for k in range(i,j):
            q = m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
            if(q<m[i][j]):
                m[i][j] = q#更新权重
                s[i][j] = k#更新断开位置

print(m[0][n-1])#输出最优解次数
def brack(s,i,j):
    if(i==j):
        print("A%i"%(i+1),end='')
    else:
        print("(",end='')
        brack(s,i,s[i][j])
        brack(s,s[i][j]+1,j)
        print(")",end='')

brack(s,0,n-1)
'''
【样例1输入】
30 35 15 5 10 20 25
【样例1输出】
15125
((A1(A2A3))((A4A5)A6))
【样例说明】
 输入：第1个矩阵的行数和第1个矩阵到第6个矩阵的列数，以一个空格分隔。
 输出：矩阵连乘A1...An的最少数乘次数为15125，最优计算次序为((A1(A2A3))((A4A5)A6))。
'''