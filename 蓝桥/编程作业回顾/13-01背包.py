c = int(input())
n = int(input())
s1 = input().split()
s2 = input().split()
v = [0]
for i in s1:
    v.append(int(i))#物品价值
w = [0]
for i in s2:
    w.append(int(i))#物品质量
m = [[0 for i in range(c+1)]for i in range(n+1)]#n+1行c+1列.但第0行无意义

jmax = min(w[n]-1,c)
for j in range(0,jmax+1):
    m[n][j] = 0
for j in range(w[n],c+1):
    m[n][j] = v[n]

for i in range(n-1,1,-1):
    jmax = min(w[i]-1,c)
    for j in range(0,jmax+1):
        m[i][j] = m[i+1][j]
    for j in range(w[i],c+1):
        m[i][j] = max(m[i+1][j],m[i+1][j-w[i]]+v[i])
#物品个数在2个及以上
if(n>=2):
    m[1][c]=m[2][c]
    if(c>=w[1]):
        m[1][c] = max(m[1][c],m[2][c-w[1]]+v[1])

print(m[1][c])

x = [0 for i in range(n+1)]

for i in range(1,n):
    if(m[i][c]!=m[i+1][c]):
        x[i] = 1
        c = c-w[i]
if(m[n][c]!=0):
    x[n] = 1
else:
    x[n] = 0

for i in range(1,n+1):
    if(x[i]!=0):
        print(i,end=' ')
        flag=1
'''
【样例输入】
 10
 5
 6 3 5 4 6
 2 2 6 5 4
【样例输出】
15
1 2 5
【样例说明】
 输入：背包容量10、物品数量5、每件物品价值6, 3, 5, 4, 6和重量2, 2, 6, 5, 4。
 输出：最优解时选择物品的价值总和为15，编号为1,2,5。
 '''