# 暂存

'''
将n包糖果分给m个小朋友。
每包糖果都要分出去，每个小朋友至少要分一包，也可以多包

糖果从1到n编号，第i包糖果中wi。小朋友从1到m编号。
每个小朋友只能分到编号连续的糖果。

一个合适的方案使每个人得到的糖果差不多重。为了更好分配，可以再买一份糖果。
让某一些编号的糖果有两份。当某个编号的糖果有两份时，一个人只能最多有一份

输出：最有情况下，小朋友分到的糖果的最大重量和最小重量的差
'''

n = int(input()) #糖果的数量
m = int(input()) #小朋友的数量
w = [0 for i in range(n)]
sumSweet = [0 for i in range(n)]
dp = [[ [0 for i in range(n)]for j in range(n)] for k in range(n)]

# dp[i][j][k]
#第i个小朋友，获得的最后一颗糖是j
# 第i-1个人取到的糖果的最后一个小于等于k。
t = 0
maxW = 0
s = input().split(' ')
for i in range(n):
    w[i] = s[i] #单个糖果的质量
    if(w[i]>maxW):maxW = w[i]
    t = t+w[i] #记录总质量
    sum[i] = t  #记录从1到i的重量。
max_sum = t*2/(m-1)
maxW = max(maxW,max_sum) #每个小朋友分到的最大重量应该在这个区间

ans = float('inf') #正无穷
max_v = max_sum
while(max_v>=maxW):
    dp[0][0][0] = max_v
    for i in range(m): #一共m和小朋友
        for j in range(n): #第i个小朋友获得的最后一颗糖
            for k in range(j): #第i个小朋友获得的第一个糖，肯定在最后一个之前
                dp[i][j][k] = dp[i][j][k-1] #
                for kk in range(k,-1,-1):
                    if(sum[j]-sum[kk]<max_v):
                        dp[i][j][k] = max(dp[i][j][k],min(dp[i-1][k][kk],sum[j]-sum[kk]))
                        if(i==m and j==n):
                            ans = min(ans,max_v-dp[i][j][k])
    max_v -= 1

print(ans) #最大值和最小值的差。