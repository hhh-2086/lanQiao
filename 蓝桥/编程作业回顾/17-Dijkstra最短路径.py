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
            if(data[key][col]+min_node.value<Node[index].value):
                Node[index].value = data[key][col]+min_node.value
                Node[index].pre = min_node

result = sorted(result,key=lambda i:i.own)#将结果按照结点排序
def find(mes):
    if(mes.value==float('inf')):
        print('inf: 1->'+str(mes.own+1))
        return
    flag = str(mes.own+1)
    pathlen = mes.value
    while(mes.own!=0):
        mes = mes.pre
        flag = str(mes.own+1)+'->'+flag
    flag = str(pathlen)+': '+flag
    print(flag)

for i in result[1:]:
    find(i)

'''
【样例输入】
5
0 10 0 30 100
0 0 50 0 0
0 0 0 0 10
0 0 20 0 60
0 0 0 0 0
【样例输出】
10: 1->2#到2的最短路径
50: 1->4->3#到3的最短路径
30: 1->4
60: 1->4->3->5
'''