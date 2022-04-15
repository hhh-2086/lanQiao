'''
6x6的方格，沿着格子的边线剪开成两部分。要求这两部分的形状完全相同。
试计算：包括这3种分法在内，一共有多少种不同的分割方法。注意：旋转对称的属于同一种分割

'''

# 正确答案：509

# 上下左右四个方向

dire = ((-1,0),(1,0),(0,-1),(0,1))
mapData = [[0 for i in range(7)]for j in range(7)]

result = 0
def dfs(x,y):
    if(x==0 or y==0 or x==6 or y==6):
        global result
        result+=1 #剪到了边缘。
        return
    
    mapData[x][y] = 1
    mapData[6-x][6-y] = 1

    for k in range(4):
        nx = x+dire[k][0]
        ny = y+dire[k][1]

        if(nx<0 or ny<0 or nx>6 or ny>6):
            continue
        if(mapData[nx][ny]==0):
            dfs(nx,ny)

    # 最后进行回溯
    # 清空来时的路径。让其他路线的访问，
    # 因为dfs一直走到头，下次不会再次访问
    mapData[x][y] = 0
    mapData[6-x][6-y] = 0

dfs(3,3)#从中心开始
print(result/4)

# 输出 509