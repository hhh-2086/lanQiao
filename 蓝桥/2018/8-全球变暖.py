mapData = []
N = int(input())
for i in range(N):
    s = input()
    row = []
    for j in range(N):
        row.append([s[j],0])
    mapData.append(row)

def bfs(i,j):
    # 在广度优先遍历过程中，应该访问连续的陆地
    # 并且最后如果岛屿完全淹没的话，应该返回1
    road = [(i,j)]
    ret = 1 #默认岛屿会被淹没
    while(len(road)!=0):
        (i,j) = road.pop(0)#将元素抛出
        # 将该元素周围的陆地点，抛入road中
        # 上方的像素点
        if(mapData[i-1][j][0]=='#' and mapData[i+1][j][0]=='#' and mapData[i][j-1][0]=='#' and mapData[i][j+1][0]=='#'):
            ret = 0 #出现最后不会被淹没的像素点
        if(mapData[i-1][j][0]=='#' and mapData[i-1][j][1]==0):
            mapData[i-1][j][1] = 1
            road.append((i-1,j))
        # 下
        if(mapData[i+1][j][0]=='#' and mapData[i+1][j][1]==0):
            mapData[i+1][j][1] = 1
            road.append((i+1,j))
        # 左
        if(mapData[i][j-1][0]=='#' and mapData[i][j-1][1]==0):
            mapData[i][j-1][1] = 1
            road.append((i,j-1))
        # 右
        if(mapData[i][j+1][0]=='#' and mapData[i][j+1][1]==0):
            mapData[i][j+1][1] = 1
            road.append((i,j+1))
    
    return ret

result = 0
for i in range(1,N-1):
    for j in range(1,N-1):
        if(mapData[i][j][0]=='#' and mapData[i][j][1]==0):#是陆地并且没有被访问
            mapData[i][j][1]=1 #标记这个像素点
            result += bfs(i,j)

print(result)