'''
给定一个长度为N 的数组A = [A1, A2,…,AN]，数组中有可能有重复出现的整数。
现在小明要按以下方法将其修改为没有重复整数的数组。小明会依次修改A2, A3, …, AN。
当修改Ai 时，小明会检查Ai 是否在A1~ Ai-1 中出现过。
如果出现过，则小明会给Ai 加上1 ；
如果新的Ai 仍在之前出现过，小明会持续给Ai 加1 ，直到Ai 没有在A1~Ai-1中出现过。
当AN 也经过上述修改之后，显然A数组中就没有重复的整数了。
现在给定初始的A 数组，请你计算出最终的A 数组。

【输入】

第一行包含一个整数N(1<=N<=100000)
第二行包含N个整数A1,A2,...,AN(1<=Ai<=1000000)

【输出】
输出N个整数，依次是最终的A1,A2,...,AN

【样例输入】
5
2 1 1 3 4
【样例输出】
2 1 3 4 5
'''

MAXN=100005  
MAXA=1100005 #结果集中的最大值
# 如果一直插入1000000，那么最后的数据会超出1000000.因此查并集的值域是max（Ai）+N

N = int(input())
data = input().split()
data = list(map(lambda x:int(x),data))

markData = [0 for i in range(MAXA)]#如果某个数字占用，则标记为1
ancestor = [i for i in range(MAXA)]#记录数字所在的祖先

def find_ancestor(x):
    # if(ancestor[x]==x):
    #     return x
    # return find_ancestor(ancestor[x])
    #递归找到根节点
    #防止数据太大爆栈
    r = x
    while ( ancestor[r] != r ):
        r=ancestor[r]  #找到根结点
    i=x
    j=0
    while(i != r):    
        j = ancestor[i]     #用临时变量j记录
        ancestor[i]= r      #把路径上元素的集改为根结点
        i = j

    return r

ans = 0
for i in range(N):
    a = data[i]
    if(markData[a]!=0):
        ans = find_ancestor(a)+1
    else:
        ans = a

    print(ans,end=' ')#原数字对应的新数字
    markData[ans] = 1

    # 看看前后的集合是否可以合并
    if(ans!=1 and markData[ans-1]):
        ancestor[ans-1] = ans

    if(markData[ans+1]):
        ancestor[ans] = ans+1