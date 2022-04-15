'''
填入0~9的数字。要求：连续的两个数字不能相邻。
（左右、上下、对角都算相邻）

一共有多少种可能的填数方案？

请填写表示方案数目的整数。
注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。
'''
# 相邻的点：

# 全排列问题
dire = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

mapData = [[-2 for i in range(4)] for j in range(3)]
mapData[0][0] = -3
mapData[2][3] = -3

def judgeBy(a,b,center):
    # center = mapData[a][b]
    for (i,j) in dire:
        aa = a+i
        bb = b+j
        if(aa<0 or aa>2 or bb<0 or bb>3):
            continue
        else:
            if(mapData[aa][bb]==-3):
                continue
            if(abs(mapData[aa][bb]-center)==1):
                return False
    return True

def draw(row,col,data):
    result = 0
    length = len(data)

    if(row==2 and col==3):
        return 0
    if(row==2 and col==2):  #在方格中填入最后一个数字时，只有一种情况
        if(judgeBy(row,col,data[0])):
            return 1
        else:
            return 0

    for k in range(length):
        ele = data[k]
        if(judgeBy(row,col,ele)):
            mapData[row][col] = ele #先将对应的元素填入确定位置
            data1 = data[0:k]+data[k+1:]
            if(row<=1 and col<3):
                result += draw(row,col+1,data1)
            elif(row<=1 and col==3):
                result += draw(row+1,0,data1)
            elif(row==2 and col<=1):
                result += draw(row,col+1,data1)
            mapData[row][col] = -2 #回复到原来的位置

    return result

ret = draw(0,1,[i for i in range(10)])
print(ret)
# 1580