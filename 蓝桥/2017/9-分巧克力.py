'''
 儿童节那天有K位小朋友到小明家做客。小明拿出了珍藏的巧克力招待小朋友们。
    小明一共有N块巧克力，其中第i块是Hi x Wi的方格组成的长方形。
    为了公平起见，小明需要从这 N 块巧克力中切出K块巧克力分给小朋友们。切出的巧克力需要满足：
    1. 形状是正方形，边长是整数  
    2. 大小相同  
例如一块6x5的巧克力可以切出6块2x2的巧克力或者2块3x3的巧克力。
当然小朋友们都希望得到的巧克力尽可能大，你能帮小Hi计算出最大的边长是多少么？

输入
第一行包含两个整数N和K。(1 <= N, K <= 100000)  
以下N行每行包含两个整数Hi和Wi。(1 <= Hi, Wi <= 100000) 
输入保证每位小朋友至少能获得一块1x1的巧克力。   

输出
输出切出的正方形巧克力最大可能的边长。

样例输入：

2 10  
6 5  
5 6 
 样例输出：

2
'''

N,K = input().split()
N,K = int(N),int(K)
data = []

def countNum(a,b,s):#边长a，b的长方形，能切出多少个长为s的正方形
    k1 = a//s
    k2 = b//s
    return k1*k2

min = float('inf')
for i in range(N):
    [a,b] = input().split()
    a,b = int(a),int(b)
    if(a<min):
        min = a
    if(b<min):
        min = b
    
    data.append((a,b))

tot = 0
result = 1
l = 1
r = min
# 暴力破解的方法
# for j in range(min,0,-1):
#     tot = 0
#     for i in range(N):
#         tot += countNum(data[i][0],data[i][1],j)
#     if(tot>=K):
#         result = j
#         break

while(l<=r):
    mid = (l+r)//2
    tot = 0
    for i in range(N):
        tot += countNum(data[i][0],data[i][1],mid)
    
    if(tot>=K):
        l = mid+1
        result = mid
    else:
        r = mid-1

print(result)

# 但是暴力破解会导致时间超出。
# 用二分法进行优化
