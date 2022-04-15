'''
有9只盘子，排成1个圆圈。
其中8只盘子内装着8只蚱蜢，有一个是空盘。
我们把这些蚱蜢顺时针编号为 1~8
每只蚱蜢都可以跳到相邻的空盘中，
也可以再用点力，越过一个相邻的蚱蜢跳到空盘中。
请你计算一下，如果要使得蚱蜢们的队形改为按照逆时针排列，
并且保持空盘的位置不变（也就是1-8换位，2-7换位,…），至少要经过多少次跳跃？
'''
# 转化为空盘子在跳。初始状态:12345678. 终止状态：087654321
# 广度优先搜索算法

start = ((0,1,2,3,4,5,6,7,8),0,0) #最后一个地方记录0的位置
end = [0,8,7,6,5,4,3,2,1]
# 与0所在的交换位置
preRoad = set() #纪录已经访问过的状态

result = 0
road = [start]
while(True):
    state = road.pop(0)
    position = state[1]
    depth = state[2]
    # print(state[0])
    # print(depth)
    if(position==0 and state[0]==(0,8,7,6,5,4,3,2,1)):
        result = depth
        break
    if(position-1>=0):
        s = list(state[0])
        t = s[position-1]
        s[position-1] = s[position]
        s[position] = t
        nextState = tuple(s)
        if(nextState not in preRoad):
            preRoad.add(nextState)
            road.append((tuple(s),position-1,depth+1))
    if(position-2>=0):
        s = list(state[0])
        t = s[position-2]
        s[position-2] = s[position]
        s[position] = t
        nextState = tuple(s)
        if(nextState not in preRoad):
            preRoad.add(nextState)
            road.append((tuple(s),position-2,depth+1))

    if(position+1<9):
        s = list(state[0])
        t = s[position+1]
        s[position+1] = s[position]
        s[position] = t
        nextState = tuple(s)
        if(nextState not in preRoad):
            preRoad.add(nextState)
            road.append((tuple(s),position+1,depth+1))

    if(position+2<9):
        s = list(state[0])
        t = s[position+2]
        s[position+2] = s[position]
        s[position] = t
        nextState = tuple(s)
        if(nextState not in preRoad):
            preRoad.add(nextState)
            road.append((tuple(s),position+2,depth+1))

print(result)
# 36为最终的结果