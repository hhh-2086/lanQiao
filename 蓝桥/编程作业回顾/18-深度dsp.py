from queue import LifoQueue
n = int(input())
data = [[float(i)for i in input().split()]for j in range(n)]
graph_dict = {}#创建邻接表
for i in range(n):
    value = []
    for j in range(n):
        if(data[i][j]!=0):value.append(j)
    graph_dict.update({i:value})

class node(object):
    def __init__(self,value,cost,parent = None,path = [0]):#value是结点代号，cost是起始节点到该节点的路径长度
        self.value = value
        self.cost = cost
        self.parent = parent
        self.path = path
    def __lt__(self,other):#当该类型作比较时，怎样比较
        return (self.cost<other.cost)
    def __repr__(self):
        return self.path

def print_path(path):
    s = '%i'%(path[0]+1)
    for i in path[1:]:
        s = s+'->%i'%(i+1)
    print(s)

best = [float("inf"),[]]
open = LifoQueue()
open.put(node(0,0,None,[0]))#只有根节点
close = []
n = 0
while(not open.empty()):
    cur = open.get()
    n = n+1
    if(n<=20):print_path(cur.path)
    if(cur.cost>=best[0]):continue

    children = []
    for i in list(graph_dict[cur.value]):#邻接图中找对应节点
        if(i not in cur.path):
            p = cur.path.copy()
            p.append(i)
            c =  node(i,data[cur.value][i]+cur.cost,cur,p)
            children.append(c)
    if(len(children)==0):#是叶节点
        if(cur.cost+data[cur.value][0]<best[0]):
            best[0] = cur.cost+data[cur.value][0]#更新最优解
            best[1] = cur.path
    for v in range(len(children)-1,-1,-1):
        if(children[v].cost<best[0]): open.put(children[v])#倒序加入open

print("{:.10g}: ".format(best[0]),end='')
print_path(best[1])