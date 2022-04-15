'''
X星球的一处迷宫游乐场建在某个小山坡上。它是由10x10相互连通的小房间组成的。
房间的地板上写着一个很大的字母。我们假设玩家是面朝上坡的方向站立，则：
L表示走到左边的房间，R表示走到右边的房间，U表示走到上坡方向的房间，D表示走到下坡方向的房间。
X星球的居民有点懒，不愿意费力思考。他们更喜欢玩运气类的游戏。这个游戏也是如此！
开始的时候，直升机把100名玩家放入一个个小房间内。玩家一定要按照地上的字母移动。
迷宫地图如下：
UDDLUULRUL
UURLLLRRRU
RRUURLDLRD
RUDDDDUUUU
URUDLLRRUU
DURLRLDLRL
ULLURLLRDU
RDLULLRDDD
UUDDUDUDLL
ULRDLUURRR
请你计算一下，最后，有多少玩家会走出迷宫? 而不是在里边兜圈子。
'''

mapData = [['U', 'D', 'D', 'L', 'U', 'U', 'L', 'R', 'U', 'L'], 
            ['U', 'U', 'R', 'L', 'L', 'L', 'R', 'R', 'R', 'U'], 
            ['R', 'R', 'U', 'U', 'R', 'L', 'D', 'L', 'R', 'D'], 
            ['R', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'U'], 
            ['U', 'R', 'U', 'D', 'L', 'L', 'R', 'R', 'U', 'U'], 
            ['D', 'U', 'R', 'L', 'R', 'L', 'D', 'L', 'R', 'L'], 
            ['U', 'L', 'L', 'U', 'R', 'L', 'L', 'R', 'D', 'U'], 
            ['R', 'D', 'L', 'U', 'L', 'L', 'R', 'D', 'D', 'D'], 
            ['U', 'U', 'D', 'D', 'U', 'D', 'U', 'D', 'L', 'L'], 
            ['U', 'L', 'R', 'D', 'L', 'U', 'U', 'R', 'R', 'R']]

# 不会在里面兜圈子。应该是不要走以前走过的路
def out(i,j):
    path = set()
    path.add((i,j))
    while(True):
        if(mapData[i][j]=='U'):
            i,j = i-1,j
            if(i<0):
                return True
            if((i,j) in path):
                return False
            path.add((i,j))
        elif(mapData[i][j]=='D'):
            i,j = i+1,j
            if(i>=10):
                return True
            if((i,j) in path):
                return False
            path.add((i,j))
        elif(mapData[i][j]=='R'):
            i,j = i,j+1
            if(j>=10):
                return True
            if((i,j) in path):
                return False
            path.add((i,j))
        else:
            i,j = i,j-1
            if(j<0):
                return True
            if((i,j) in path):
                return False
            path.add((i,j))
    
result = 0
for i in range(10):
    for j in range(10):
        if(out(i,j)):
            result+=1

print(result)
# 31