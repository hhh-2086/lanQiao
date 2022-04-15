'''
左孩子右兄弟表示法，转化成二叉树。
每个节点的父亲节点，比自己的数值小
最后输出的结果，是转化后的二叉树中，最高的高度是多少
'''
# 节点个数
numNode = int(input())
nodeMap = [[0 for i in range(numNode)] for j in range(numNode-1)]
# 构造关系表，行值+1为节点值，列值+1为节点的字节点编号
for i in range(numNode-1):
    var = int(input())  #var-1是父节点
    nodeMap[var-1][i+1] = 1 #i+1是子节点

# 作为父节点，其值都要小于自己孩子的节点值
# 所以前求值小的节点的dp值，然后再求节点值大的dp值
# 当节点是叶子节点时，dp值是0
# 值最大的那个节点，肯定是叶子，挂在最下方
# 该节点的儿子>2就需要转化
deep = [0 for i in range(numNode)] #n个节点的深度
# 从最大的节点开始
for i in range(numNode-2,-1,-1):
    nodeVar = i
    childSum = 0
    maxdeep = 0
    for j in range(nodeVar+1,numNode):#如果有孩子节点，孩子结点的值大于本身
        if(nodeMap[nodeVar][j]==1):#其孩子节点
            childSum += 1
            if(deep[j]>maxdeep):maxdeep = deep[j]
    deep[nodeVar] = childSum+maxdeep #孩子的数目加最大孩子的dp

print(deep[0])#即最大深度