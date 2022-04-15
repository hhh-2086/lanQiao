''''分组时的组的个数为n/5的向下取整；分组后的中位数取第（num_group/2向上取整）小的元素。'''
import math
s = input().split()
data = []
for i in s:    data.append(int(i))
k = int(input())#要找的数字的位置
global N
N = len(data)
def sort(A,p,r):#冒泡排序
    for i in range(r,p-1,-1):
        for j in range(p,i):
            if(A[j]>A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if(A[j]<=x):
            i=i+1
            t = A[j]
            A[j] = A[i]
            A[i] = t
    t = A[i+1]#基准元素与最后一个元素交换位置
    A[i+1] = A[r]
    A[r] = t
    return i+1
#中位数为划分基准
def select(A,p,r,k):
    size = r-p+1
    if(size<=5):
        #sort(A,p,r)
        A[p:r+1] = sorted(A[p:r+1])
        return A[p+k-1]#根据i的偏移位置返回。因为递归时需要的位置在变化。

    b = []
    for i in range(p,r,5):
        if(i+4<=r):
            b.append(select(A,i,i+4,3))#将列表切片递归找到每小组的中位数。
    x = select(b,0,len(b)-1,math.ceil(len(b)/2))#将每小组中位数的中位数递归找中位数
    if(r-p+1==N):print(x)#第一次的基准元素输出
  
    c = A.index(x)
    A[c],A[r]=A[r],A[c]
    q = partition(A,p,r)

    i = q-p+1
    if(i == k):
        return A[q]
    elif(k<i):
        return select(A,p,q-1,k)
    else:
        return select(A,q+1,r,k-i)

x = select(data,0,len(data)-1,k)
print(x)
'''
【样例输入】
 2 9 8 0 7 10 1 12 3 14 5 13 6 11 4
 3
【样例输出】
7 
2
【样例说明】
 输入：15个整数，以空格分隔。要寻找第3小元素。
 输出：
7，表示第一次划分得到的基准元素是7。
2，表示第3小元素为2。
'''