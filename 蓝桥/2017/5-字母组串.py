'''
题目：

由 A,B,C 这3个字母就可以组成许多串。
比如：“A”,“AB”,“ABC”,“ABA”,“AACBB” …

现在，小明正在思考一个问题：
如果每个字母的个数有限定，能组成多少个已知长度的串呢？

输入：
a个A，b个B，c个C 字母，能组成多少个不同的长度为n的串。

输出一个数表示结果
'''
# 该题是代码填空题

def f(a,b,c,n):
    if(a<0 or b<0 or c<0):
        return 0
    if(n==0):
        return 1
    # return 后面的代码是填空
    # 三种递归方案
    return f(a-1,b,c,n-1)+f(a,b-1,c,n-1)+f(a,b,c-1,n-1)

print(f(1,1,1,2))