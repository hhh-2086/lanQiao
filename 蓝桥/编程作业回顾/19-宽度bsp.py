from queue import Queue
n = int(input())
data = [[float(i)for i in input().split()]for j in range(n)]
graph_dict = {}#创建邻接表
for i in range(n):
    value = []
    for j in range(n):
        if(data[i][j]!=0):value.append(j)
    graph_dict.update({i:value})

class node(object):
    def __init__(self,value,cost,parent = None,path = None):#value是结点代号，cost是起始节点到该节点的路径长度
        self.value = value
        self.cost = cost
        self.parent = parent
        self.path = path
    def __lt__(self,other):#当该类型作比较时，怎样比较
        return (self.cost<other.cost)

def print_path(path):
    s = '%i'%(path[0]+1)
    for i in path[1:]:
        s = s+'->%i'%(i+1)
    print(s)

Node = node(0,0,None,[0])#根节点
##深度优先查找
best = [float("inf"),[]]
open = Queue()
open.put(Node)
close = []
n = 0
while(not open.empty()):
    cur = open.get()
    n = n+1
    if(n<=20):print_path(cur.path)
    if(cur.cost>=best[0]):continue

    clength=0#可以导入几个结点
    for i in list(graph_dict[cur.value]):#邻接图中找对应节点
        if(i not in cur.path):
            p = cur.path.copy()
            p.append(i)
            c =  node(i,data[cur.value][i]+cur.cost,cur,p)
            clength=clength+1
            if(c.cost<best[0]): open.put(c)#顺序加入open
    if(clength==0):#是叶节点
        if(cur.cost+data[cur.value][0]<best[0]):
            best[0] = cur.cost+data[cur.value][0]#更新最优解
            best[1] = cur.path

print("{:.10g}: ".format(best[0]),end='')
print_path(best[1])