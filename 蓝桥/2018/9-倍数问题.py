'''
众所周知，小葱同学擅长计算，尤其擅长计算一个数是否是另外一个数的倍数。但小葱 只擅长两个数的情况，当有很多个数之后就会比较苦恼。现在小葱给了你 n 个数，希望你 从这 n 个数中找到三个数，使得这三个数的和是 K 的倍数，且这个和最大。数据保证一 定有解。

输入
从标准输入读入数据。 第一行包括 2 个正整数 n,K。
第二行 n 个正整数，代表给定的n 个数。
输出
输出到标准输出。 输出一行一个整数代表所求的和。

样例
输入
4 3
1 2 3 4
输出
9

数据约定
对于 30% 的数据，n <= 100。
对于 60% 的数据，n <= 1000。
对于另外 20% 的数据，K <= 10。
对于 100% 的数据，1 <= n <= 105, 1 <= K <= 103，给定的 n 个数均不超过 108。
'''
# 关于取余运算的性质：(a+b+c)%k = (a%k+b%k+c%k)%k
n,k = input().split()
n,k = int(n),int(k)
data = list(map(lambda x:int(x),input().split()))

# 余数是从0开始的，余数只有0到k-1
# 预处理部分
dealData = [[0,0,0]for i in range(k)]
for i in range(n):
    row = data[i]%k
    if(dealData[row][2]<data[i]):
        dealData[row][2] = data[i] #最后一个是最小值。
    dealData[row] = sorted(dealData[row],reverse=True)

result = 0 
for i in range(k):
    aa = 0
    bb = 0
    cc = 0
    if(dealData[i][0]==0):continue
    aa = dealData[i][0]
    for j in range(i,k):
        if(i==j):
            if(dealData[i][1]==0):continue
            else:bb = dealData[j][1]
        else:
            bb = dealData[j][0]

        c = (((i+j)//k+1)*k-i-j)%k  #定位第三个余数所在的位置

        # print(c)
        if(dealData[c][0]==0):continue  #具有该余数的不存在
        
        if(c==i or c==j):
            if(c==i and c==j):
                if(dealData[c][2]==0):continue
                cc = dealData[c][2]
            else:
                cc = dealData[c][1]
        else:
            cc = dealData[c][0]

        tot = aa+bb+cc
        if(tot>result):result = tot

print(result)