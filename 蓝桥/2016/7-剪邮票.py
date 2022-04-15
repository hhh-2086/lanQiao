'''
如【图1.jpg】, 有12张连在一起的12生肖的邮票。
现在你要从中剪下5张来，要求必须是连着的。
（仅仅连接一个角不算相连）
比如，【图2.jpg】，【图3.jpg】中，粉红色所示部分就是合格的剪取。


请你计算，一共有多少种不同的剪取方法。
'''


# 正确答案：116

dire = ((-1,0),(1,0),(0,-1),(0,1))

map = [[0 for i in range(4)] for j in range(3)]

data = {}
result = 0
def dfs(g,i,j):
    g[i][j] = 0  #将遍历初始点，由1设置为0
    for k in range(4):
        a = i+dire[k][0]
        b = j+dire[k][1]
        if(a<0 or b<0 or a>2 or b>3):
            continue
        else:
            if(g[a][b]==1):
                dfs(g,a,b)

def check(ele):
    g = [[0 for i in range(4)]for j in range(3)]
    for i in range(3):
        for j in range(4):
            if(ele[i*4+j]==1):
                g[i][j] = 1
    
    cnt = 0 #连通块的个数
    for i in range(3):
        for j in range(4):
            if(g[i][j]):
                dfs(g,i,j)
                cnt += 1
    
    return cnt==1 #如果只有一个连通块，那就是正确的
    # 转化成二维矩阵

# 全排列
stamp = [1,1,1,1,1,0,0,0,0,0,0,0]
choice = set()
result = 0
import itertools
for ele in itertools.permutations(stamp,12):
    string = ''
    for i in ele:
        string+=str(i)
    if(string in choice):
        continue
    else:
        choice.add(string) #添加新的组合
        if(check(ele)):
            result+=1
            print(result)

print(result)
# 116.好像运行了几十分钟。保守估计20min