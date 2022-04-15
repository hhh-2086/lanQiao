'''
给 n, m, k，求有多少对( i , j )满足1 ≤ i ≤ n , 0 ≤ j ≤ min ( i , m )
且Cj i ≡ 0 ( mod k)，k 是质数。
其中 Cj i 是组合数，表示从 i 个不同的数中选出 j 个组成一个集合的方案数。

输入：第一行两个数 t, k，其中 t 代表该测试点包含 t 组询问，
    k 的意思与上文中 相同。

接下来 t 行每行两个整数 n, m，表示一组询问。

输出：输出 t 行，每行一个整数表示对应的答案。
由于答案可能很大，请输出答 案除以 10^9 + 7的余数。
'''
# 卢卡斯定理
import math
# 据说该运算会加快速度。
def Lucas(n,m,p):
    if(m==0):
        return 1
    else:
        return (math.comb(n % p, m % p) * Lucas(n // p, m // p, p)) % p

# k是质数。最小的质数是2
data = [[  [1,0]  ]]#杨辉三角的值
mark = [0]#记录杨辉三角一行中所有能整除的数量。方便统计计算，不用向上遍历
# 目前杨辉三角的行的值：
row = 0
t,k = input().split()
t,k = int(t),int(k)
for i in range(t):
    n,m = input().split()
    n,m = int(n),int(m)

    if(n>row):
        for i in range(row+1,n+1):
            e = [[1,0]]
            sum = 0
            for j in range(1,i):
                re = (data[i-1][j][0]+data[i-1][j-1][0])%k
                e.append([re,e[j-1][1]])
                if(re==0):
                    e[j][1] += 1
                    sum+=1#记录一行中被整除的元素的个数
                    
            e.append([1,e[-1][1]])
            data.append(e)
            mark.append(sum+mark[i-1])
    
    # 然后开始向上求最后的结果，如果m<n，那就要向上求解。如果m>=n，直接加上mark在该处的值
    result = 0
    nn = n
    while(m<nn):
        result += data[nn][m][1]
        nn -= 1

    result += mark[nn]
    print(result)