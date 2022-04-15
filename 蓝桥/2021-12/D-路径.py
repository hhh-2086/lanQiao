# 构造出整个图，最小公倍数 = a*b/gcd(a,b)
# 最短路径算法
'''
小蓝学习了最短路径之后特别高兴，他定义了一个特别的图，希望找到图中的最短路径。

小蓝的图由 2021 个结点组成，依次编号 1 至 2021。

对于两个不同的结点 a, b，如果 a 和 b 的差的绝对值大于 21，则两个结点之间没有边相连；
如果 a 和 b 的差的绝对值小于等于 21，则两个点之间有一条长度为 a 和 b 的最小公倍数的无向边相连。

例如：结点 1 和结点 23 之间没有边相连；结点 3 和结点 24 之间有一条无向边，长度为 24；结点 15 和结点 25 之间有一条无向边，长度为 75。

请计算，结点 1 和结点 2021 之间的最短路径长度是多少。

提示：建议使用计算机编程解决问题。
'''
#答案：10266837


def gcd(a,b):
    if(b):
        return gcd(b,a%b)
    return a
# 最小公倍数
def maxM(a,b):
    return a*b//gcd(a,b)

# 构建无向图
# 如果最后的值为0，说明两个节点之间没有路
map = [[0 for j in range(2021)] for i in range(2021)]
for i in range(2021):
    for j in range(2021):
        if(abs(i-j)<=21 and i!=j):
            map[i][j] = maxM(i+1,j+1)

# 最短路径算法

def minPath(map):
    n = len(map) #节点的个数
    node = [float('inf') for i in range(n)] #初始化每一个节点到最初节点的最短路径
    node[0] = 0 #最开始的节点到自己的距离是0
    road = [0]  #作为一个栈，存储的是待开发节点
    while(len(road)):
        t = road.pop(0)#将最开端的节点抛出
        m = t-21
        if(m<0):m = 0
        m2 = t+22
        if(m2>n):m2 = n
        for j in range(m,m2): #只有这个范围有边且肯定有边，小于自己21以内和大于自己21以内的
            if(t==j):continue
            if(node[t]+map[t][j]<node[j]):
                road.append(j)
                node[j] = node[t]+map[t][j]
    return node[-1] #返回第一个节点到最后一个节点的最短路径

print(minPath(map))
# 输出 10266837