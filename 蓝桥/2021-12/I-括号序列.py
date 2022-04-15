'''
给定一个括号序列，要求尽可能少的添加考好使得括号序列变得合法
例如对于（（（），添加两个括号就会合法：
    （）（）（）、（）（（））、（（））（）、（（）（））和（（（）））
输入串：（和）
输出格式：n为最终序列的数目，请输出n除以1000000007的余数
'''

Sinput = input() #输入的字符串

def countLR(Sinput):
    cntL = 0 #最终需要的左括号的数量
    cntR = 0 #最终需要的右括号的数量
    for i in Sinput:
        if(i=='('):
            cntR += 1
        else:
            cntR -=1
            if(cntR<0):
                cntL += 1
                cntR += 1
    return cntR,cntL


def findResult(Sinput,col):
    strLen = len(Sinput)
    dataMap = [[0 for i in range(strLen+2)] for  j in range(strLen+1)]

    dataMap[0][0] = 1
    
    # 第一行除了0，0是1，其他都是0
    for i in range(1,strLen+1):
        if(Sinput[i-1]=="("):
            for j in range(1,strLen+1):
                dataMap[i][j] = dataMap[i-1][j-1]
        else:
            dataMap[i][0] = dataMap[i-1][0]+dataMap[i-1][1]
            for j in range(1,strLen+1):
                dataMap[i][j] = dataMap[i-1][j+1]+dataMap[i][j-1]

# 两种方式定位，一种是遍历，第一处不是0的，就是恰好匹配时的策略值。一种是得到col。直接定位，但需要函数计算
    # for i in dataMap[strLen]: #遍历最后一行
    #     if(i!=0):
    #         return i
    return dataMap[strLen][col]
def reverse(Sinput):
    result = ''
    for i in Sinput[-1::-1]:
        if(i=='('):
            result += ')'
        else:
            result += '('
    return result

cntR,cntL = countLR(Sinput)
#需要补充的右括号的数目，就是补充完左括号之后，余下的左括号的数目。
# 如果进行这一步，可以直接定位最终值所在的位置
reL = findResult(Sinput,cntR)
Sinput = reverse(Sinput)
reR = findResult(Sinput,cntL)

print(reL*reR)