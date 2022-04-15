'''
“饱了么”外卖系统中维护着N 家外卖店，编号1~N。每家外卖店都有一个优先级，初始时(0 时刻) 优先级都为0。
每经过1 个时间单位，如果外卖店没有订单，则优先级会减少1，最低减到0；
而如果外卖店有订单，则优先级不减反加，每有一单优先级加2。
如果某家外卖店某时刻优先级大于5，则会被系统加入优先缓存中；如果优先级小于等于3，则会被清除出优先缓存。

给定T 时刻以内的M 条订单信息，请你计算T 时刻时有多少外卖店在优先缓存中。


【输入】
第一行包含3 个整数N、M 和T。
以下M 行每行包含两个整数ts 和id，表示ts 时刻编号id 的外卖店收到一个订单
1<=N, M, T<=100000，1<=ts<=T，1<=id<=N。


【输出】

输出一个整数代表答案。
【样例输入】
2 6 6
1 1
5 2
3 1
6 2
2 1
6 2
【样例输出】
1
'''

N,M,T = input().split()
N,M,T = int(N),int(M),int(T)
# T时刻以内的，M条订单。计算T时刻有多少外卖店在优先缓存中
# 以下是ts时刻编号id的外卖店收到一个订单
data = []
for i in range(M):
    s = input().split()
    data.append( (int(s[0]),int(s[1])) )

data = sorted(data,key=lambda x:x[0])

remarkData =[ [0 for i in range(N)] for j in range(T)]

for i in data:
    remarkData[i[0]-1][i[1]-1] += 1

result = {}
# 也可以用set集合。应该容易确定某个元素是否在缓存区中

for j in range(N):
    remarkData[0][j] = remarkData[0][j]*2
    if(remarkData[0][j]>5):
        result.update({j:remarkData[0][j]})

for i in range(1,T):
    for j in range(N):
        if(remarkData[i][j]!=0):
            remarkData[i][j] = remarkData[i][j]*2+remarkData[i-1][j]
            if(remarkData[i][j]>5):
                result.update({j:remarkData[i][j]})
        else:
            if(remarkData[i-1][j]!=0):
                remarkData[i][j] = remarkData[i-1][j]-1
                if(remarkData[i][j]<=3 and result.get(j,None)!=None):
                    result.pop(j) #在缓存中抛出

ret = list(result.keys())
print(len(ret))
