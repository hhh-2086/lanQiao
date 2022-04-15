'''
class node(object):
    def __init__(self,own,value):
        self.own = own
        self.value = value

    def __lt__(self,other):
        return (self.value<other.value)

Node = [node(1,2),node(2,4),node(3,3)]

for i in sorted(Node):
    print(i.value)
'''
s = [int(i) for i in input().split()]
def quickSort(s,p,r,n):
    n = n+1    #记录递归次数
    if(p<r):
        q = part(s,p,r)
        n = quickSort(s,p,q-1,n)
        n = quickSort(s,q+1,r,n)
    return n

def part(s,p,r):
    x = s[r]   #划分基准
    i = p-1
    for j in range(p,r):
        if(s[j]<=x):
            i = i+1
            s[i],s[j] = s[j],s[i] #交换i j位置的值
    s[i+1],s[r] = s[r],s[i+1]       #基准与i后面位置的值交换
    return i+1

r = len(s) - 1
N = quickSort(s,0,r,0)
print(N)
for i in s:print(i,end=' ')
