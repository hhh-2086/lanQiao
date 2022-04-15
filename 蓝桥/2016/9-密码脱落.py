'''
X星球的考古学家发现了一批古代留下来的密码。
这些密码是由A、B、C、D 四种植物的种子串成的序列。
仔细分析发现，这些密码串当初应该是前后对称的（也就是我们说的镜像串）。
由于年代久远，其中许多种子脱落了，因而可能会失去镜像的特征。
你的任务是：
给定一个现在看到的密码串，计算一下从当初的状态，它要至少脱落多少个种子，才可能会变成现在的样子。

输入一行，表示现在看到的密码串（长度不大于1000）
要求输出一个正整数，表示至少脱落了多少个种子。

例如，输入：
ABCBA
则程序应该输出：
0

再例如，输入：
ABDCDCBABC

则程序应该输出：
3
'''
# 最少添加多少字符，使现在的字符串对称
# ABDCDCBABC变为：以及其反串：
# CBABCDCDCBABC
# CBABCDCDCBABC

origineS = input()
adverseS = origineS[-1::-1]
length = len(origineS)

data = [[0 for i in range(length+1)] for j in range(length+1)]

def func():
    for i in range(1,length+1):
        for j in range(1,length+1):
            if(origineS[i-1]==adverseS[j-1]):
                data[i][j] = data[i-1][j-1]+1
            else:
                if(data[i-1][j]>data[i][j-1]):
                    data[i][j] = data[i-1][j]
                else:
                    data[i][j] = data[i][j-1]

func()
# print("字符串长度是：",length)
print(length-data[length][length])