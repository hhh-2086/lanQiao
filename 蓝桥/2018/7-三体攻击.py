'''
三体人将对地球发起攻击。为了抵御攻击，地球人派出了 A × B × C 艘战舰，
在太空中排成一个 A 层 B 行 C 列的立方体。
其中，第 i 层第 j 行第 k 列的战舰（记为战舰 (i, j, k)）的生命值为 d(i, j, k)。

三体人将会对地球发起 m 轮“立方体攻击”，
每次攻击会对一个小立方体中的所有战舰都造成相同的伤害。
具体地，第 t 轮攻击用 7 个参数 lat, rat, lbt, rbt, lct, rct, ht 描述；
所有满足 i ∈ [lat, rat],j ∈ [lbt, rbt],k ∈ [lct, rct] 的战舰 
(i, j, k) 会受到 ht 的伤害。
如果一个战舰累计受到的总伤害超过其防御力，那么这个战舰会爆炸。
地球指挥官希望你能告诉他，第一艘爆炸的战舰是在哪一轮攻击后爆炸的。

输入
第一行包括 4 个正整数 A, B, C, m；
第二行包含 A × B × C 个整数，其中第 ((i − 1)×B + (j − 1)) × C + (k − 1)+1 个数为 d(i, j, k)；
第 3 到第 m + 2 行中，第 (t − 2) 行包含 7 个正整数 lat, rat, lbt, rbt, lct, rct, ht。
A × B × C ≤ 10^6, m ≤ 10^6, 0 ≤ d(i, j, k), ht ≤ 10^9。

输出
输出第一个爆炸的战舰是在哪一轮攻击后爆炸的。保证一定存在这样的战舰。

样例输入
2 2 2 3
1 1 1 1 1 1 1 1
1 2 1 2 1 1 1
1 1 1 2 1 2 1
1 1 1 1 1 1 2

样例输出
2
'''


# 暴力破解可以得到70%的分数
'''
A,B,C,m = input().split()
A,B,C,m = map(lambda x:int(x),[A,B,C,m])

defence_ori = input().split()
defence_ori = list(map(lambda x:int(x),defence_ori))

defence = [[[0 for i in range(C)] for j in range(B)]for k in range(A)]
# 求解防御的值
for i in range(A):
    for j in range(B):
        for k in range(C):
            num = ((i-1)*B + (j-1))*C + (k-1)+1
            defence[i][j][k] = defence_ori[num]
force = [list(map(lambda x:int(x),input().split()))for i in range(m)]

def func():
    for mm in range(m):
        [lat, rat, lbt, rbt, lct, rct, ht] = force[mm]
        # i ∈ [lat, rat],j ∈ [lbt, rbt],k ∈ [lct, rct] 的战舰 (i, j, k) 会受到 ht 的伤害
        for i in range(lat,rat+1):
            for j in range(lbt,rbt+1):
                for k in range(lct,rct+1):
                    if(i>=A or j>=B or k>=C):
                        continue
                    defence[i][j][k] -= ht
                    if(defence[i][j][k]<0):
                        return mm+1

print(func())
'''
