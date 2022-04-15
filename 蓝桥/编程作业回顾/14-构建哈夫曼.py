import heapq
import queue
n = int(input())
data = [int(i) for i in input().split()]

class hnode(object):
    def __init__(self,char=' ',freq=0,left=None,right=None,code=''):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = code
    def __repr__(self):#输出改类型时怎么样输出
        return("({} {})".format(self.char,self.freq))
    def __lt__(self,other):#当该类型作比较时，怎样比较
        return (self.freq<other.freq)
    def __add__(self,other):#该类型的加法
        self.code='0'
        other.code='1'
        return hnode(self.char+other.char,self.freq+other.freq,self,other)

heap = [hnode(chr(i+ord('a')),data[i])for i in range(n)]
heapq.heapify(heap)
while(len(heap)!=1):#创建好二叉树
    heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap))

#广度优先遍历重新生成每个节点的编码，并将叶子保存到s对应的codes中
s = [chr(i+ord('a')) for i in range(n)]
codes = ['' for i in range(n)]
q = queue.Queue()
q.put(heap[0])

while(q.qsize()!=0):
    r = q.get()
    if(not r.left==None):#如果结点有孩子结点，则改变孩子结点对应的编码
        r.left.code = r.code+r.left.code
        r.right.code = r.code+r.right.code
        q.put(r.left)
        q.put(r.right)
    else:
        char = r.char
        codes[s.index(char)] = r.code

for i in range(n):
    print(s[i],codes[i])