# 正确答案：DDDDRRURRRRRRDRRRRDDDLDDRDDDDDDDDDDDDRDDRRRURRUURRDDDDRDRRRRRRDRRURRDDDRRRRUURUUUUUUULULLUUUURRRRUULLLUUUULLUUULUURRURRURURRRDDRRRRRDDRRDDLLLDDRRDDRDDLDDDLLDDLLLDLDDDLDDRRRRRRRRRDDDDDDRR
mapData = ["01010101001011001001010110010110100100001000101010",
    '00001000100000101010010000100000001001100110100101',
    '01111011010010001000001101001011100011000000010000',
    '01000000001010100011010000101000001010101011001011',
    '00011111000000101000010010100010100000101100000000',
    '11001000110101000010101100011010011010101011110111',
    '00011011010101001001001010000001000101001110000000',
    '10100000101000100110101010111110011000010000111010',
    '00111000001010100001100010000001000101001100001001',
    '11000110100001110010001001010101010101010001101000',
    '00010000100100000101001010101110100010101010000101',
    '11100100101001001000010000010101010100100100010100',
    '00000010000000101011001111010001100000101010100011',
    '10101010011100001000011000010110011110110100001000',
    '10101010100001101010100101000010100000111011101001',
    '10000000101100010000101100101101001011100000000100',
    '10101001000000010100100001000100000100011110101001',
    '00101001010101101001010100011010101101110000110101',
    '11001010000100001100000010100101000001000111000010',
    '00001000110000110101101000000100101001001000011101',
    '10100101000101000000001110110010110101101010100001',
    '00101000010000110101010000100010001001000100010101',
    '10100001000110010001000010101001010101011111010010',
    '00000100101000000110010100101001000001000000000010',
    '11010000001001110111001001000011101001011011101000',
    '00000110100010001000100000001000011101000000110011',
    '10101000101000100010001111100010101001010000001000',
    '10000010100101001010110000000100101010001011101000',
    '00111100001000010000000110111000000001000000001011',
    '10000001100111010111010001000110111010101101111000']
# 传入的位置是迷宫图的第几行第几列
N = len(mapData)
M = len(mapData[0])
K = M
mapMark = [[['',float('inf')] for i in range(M)]for j in range(N)]
mapMark[0][0] = ('S',0)
import sys
sys.setrecursionlimit(100000) #例如这里设置为十万
result = ''
# N,M表示行和列
def findOut(row,col):
    if(row==N-1 and col==M-1):
        print("成功找到")
        return
    # 首先看向下方
    if( row+1<N and mapMark[row+1][col][1]>mapMark[row][col][1]+1 and mapData[row+1][col]=='0'):
        mapMark[row+1][col][0] = 'U'
        mapMark[row+1][col][1] = mapMark[row][col][1]+1
        findOut(row+1,col)
    # 向左走    
    if( col-1>=0 and mapMark[row][col-1][1]>mapMark[row][col][1]+1 and  mapData[row][col-1]=='0'):
        mapMark[row][col-1][0] = 'R'
        mapMark[row][col-1][1] = mapMark[row][col][1]+1
        findOut(row,col-1)
    # 向右走
    if( col+1<M and mapMark[row][col+1][1]>mapMark[row][col][1]+1 and mapData[row][col+1]=='0'):
        mapMark[row][col+1][0] = 'L'
        mapMark[row][col+1][1] = mapMark[row][col][1]+1
        findOut(row,col+1)
    # 向上走
    if( row-1>=0 and mapMark[row-1][col][1]>mapMark[row][col][1]+1 and  mapData[row-1][col]=='0'):
        mapMark[row-1][col][0] = 'D'
        mapMark[row-1][col][1] = mapMark[row][col][1]+1
        findOut(row-1,col)

findOut(0,0)

result  = ''

i,j = N-1,M-1
count = 0
while(count<300):
    count+=1
    if(mapMark[i][j][0]=='U'):
        i,j = i-1,j
        result+='D'
        # print(i,j)
    elif(mapMark[i][j][0]=='L'):
        i,j = i,j-1
        result+='R'
        # print(i,j)
    elif(mapMark[i][j][0]=='R'):
        i,j = i,j+1
        result+='L'
        # print(i,j)
    elif(mapMark[i][j][0]=='D'):
        i,j = i+1,j
        result+='U'
        # print(i,j)
    if(i==0 and j==0):break
print(count)
print(result[-1::-1])
