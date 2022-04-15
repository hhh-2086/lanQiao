'''
给定一棵包含N 个节点的完全二叉树，树上每个节点都有一个权值，按从上到下、
从左到右的顺序依次是A1, A2, ...，AN，如下图所示：

现在小明要把相同深度的节点的权值加在一起，他想知道哪个深度的节点
权值之和最大？如果有多个深度的权值和同为最大，请你输出其中最小的深度。
注：根的深度是1。。

【输入】
第一行包含一个整数N。
第二行包含N 个整数A1, A2,..., AN
对于所有评测用例，1<=N<=100000, -100000<=Ai<=100000。
【输出】
输出一个整数代表答案。

【样例输入】

7
1 6 5 4 3 2 1
【样例输出】
2
'''

from math import ceil, log2

n = int(input())
weight = list(map(lambda i:int(i),input().split()))
lenght = len(weight)

d = ceil(log2(n+1))
result = [0,0]
for i in range(d):#二叉树的深度
    sum = 0
    for j in range(2**i-1,2**(i+1)-1):
        if(j>=lenght):
            break
        sum+=weight[j]
    if(sum>result[1]):
        result[0] = i+1
        result[1] = sum

print(result[0])
