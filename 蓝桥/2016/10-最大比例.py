'''
X星球的某个大奖赛设了M级奖励。每个级别的奖金是一个正整数。
并且，相邻的两个级别间的比例是个固定值。
也就是说：所有级别的奖金数构成了一个等比数列。比如：
16,24,36,54
其等比值为：3/2

现在，我们随机调查了一些获奖者的奖金数。
请你据此推算可能的最大的等比值。

输入格式：
第一行为数字 N (N<100)，表示接下的一行包含N个正整数
第二行N个正整数Xi(Xi<1 000 000 000 000)，用空格分开。每个整数表示调查到的某人的奖金数额

要求输出：
一个形如A/B的分数，要求A、B互质。表示可能的最大比例系数

测试数据保证了输入格式正确，并且最大比例是存在的。

例如，输入：
3
1250 200 32

程序应该输出：
25/4

再例如，输入：
4
3125 32 32 200

程序应该输出：
5/2

再例如，输入：
3
549755813888 524288 2

程序应该输出：
4/1
'''

# 将数字从大到小排列。重复的数字去掉。
# 等比数列。缺项的等比数列
# 排序之后的，中间的比值肯定是q^k

from difflib import restore


N = int(input())
data = list(map(lambda x:int(x),input().split()))
data = sorted(data,reverse=True)

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

divS = []
num = float('inf')

# 存放每一个商，分数表示的
for i in range(len(data)-1):
    a = data[i]
    b = data[i+1]
    if(a == b):
        continue
    g = gcd(a,b)
    aa = a//g
    bb = b//g
    
    divS.append([aa,bb])

def qgcd(a,b):
    if(a==b):
        return a
    else:
        if(a<b): #保证a是大的那个
            a,b = b,a
        aa = max(a//b,b)
        bb = min(a//b,b)
        return qgcd(aa,bb)
#求出所有的商之后，对所有的商的分子和分母求公因子
result1 = divS[0][0]
result2 = divS[0][1]
for (a,b) in divS[1:]:
    result1 = qgcd(result1,a)
    result2 = qgcd(result2,b)

print(result1,end='')
print('/',end='')
print(result2)