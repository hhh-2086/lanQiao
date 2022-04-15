import heapq
n = int(input())
data =[]
for i in range(n):
    data.append([int(j) for j in input().split()])

#创建邻接表：
graph_list = {}
for i in range(len(data)):
    value = []
    for j in range(len(data)):
        if(data[i][j]!=0):value.append(j)
    graph_list.update({i:value})

class node(object):
    def __init__(self,own,value,pre=0):#本身节点，权重，前驱节点
        self.own = own
        self.value = value
        self.pre = pre
    def __repr__(self):#本身节点，前驱节点，本身权重
        return("{} {} {}".format(self.own+1,self.pre+1,self.value))
    def __lt__(self,other):#比较的方法
        return(self.value<other.value)

Node = [node(i,float('inf'))for i in range(n)]#先将所有节点初始化值为无穷
Node[0].value = 0#将第一个节点的值赋值为0
result = []
result_node = []

while(not len(Node)==0):
    heapq.heapify(Node)#每次都会导致值发生变化，重新排序
    min_node = heapq.heappop(Node)#将最小的结点抛出
    result.append(min_node)
    result_node.append(min_node.own)#只存储结点的代号
    node_own = []#记录现在Node中结点对应的代号
    for i in Node:
        node_own.append(i.own)
    key=min_node.own
    for i in list(graph_list[key]):#该节点的邻接点
        if(i not in result_node):#如果改邻接点不在结果集中，需要更新
            index = node_own.index(i)#找到该邻接点在Node中的位置
            col = Node[index].own
            if(data[key][col]<Node[index].value):
                Node[index].value = data[key][col]
                Node[index].pre = key

for i in result[1:]:#第一个结点不输出
    print(i)
'''样例输入
8
0 15 7 0 0 0 0 10
15 0 0 0 0 0 0 0  
7 0 0 9 12 5 0 0 
0 0 9 0 0 0 0 0
0 0 12 0 0 6 0 0 
0 0 5 0 6 0 14 8
0 0 0 0 0 14 0 3
10 0 0 0 0 8 3 0
【样例1输出】
3 1 7
6 3 5
5 6 6
8 6 8
7 8 3
4 3 9
2 1 15
'''