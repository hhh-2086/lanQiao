'''
RSA 是一种经典的加密算法。它的基本加密过程如下。

首先生成两个质数 p , q，令 n = p *q，设 d与 (p−1)*(q−1) 互质，
则可找到e 使得d*e 除 (p−1)*(q−1) 的余数为1。

n,d,e 组成了私钥，n,d 组成了公钥。

当使用公钥加密一个整数X 时（小于n），计算 C = X^d mod  n，
则C 是加密后的密文。( X^d 表示X的d次方)

当收到密文 C 时，可使用私钥解开，计算公式为 X =C^e  mod n。

例如，当 p = 5 , q = 11 , d = 3 时 ， n = 55 , e = 27。

若加密数字 24，得 24^3 mod 55=19。

解密数字19，得 19^27 mod 55=24。

现在你知道公钥中 n = 1001733993063167141 , d = 212353，
同时你截获了别人发送的密文 C = 20190324，请问，原文是多少？
'''

n = 1001733993063167141
d = 212353
C = 20190324
# 应该解出e的值
# 关键得到p，q。p和q都是质数
# 根据因子的性质可以知道，n除了1和本身，只有p和q两个因子。
# 因为p，q本身无法分解，所以不会生成其他因子

for i in range(2,n):
    if(n%i==0):
        p,q = i,n//i
        print(p,q)
        break
# p,q = 891234941 1123984201


# 得到p和q之后，就要计算出e
p,q = 891234941,1123984201
M = (p-1)*(q-1)
# M = 1001733991047948000
# print (M)
k = 1
ee = 0
e = 0
# 以下会判断出错，可能是由于精度产生的问题
# while(True):
#     ee = (k*M+1)/d
#     e = (k*M+1)//d
#     if(ee==e):
#         print((k*M+1)%d==0)
#         print(k)
#         break
#     k += 1
while(True):
    tmp = (k*M+1)
    if(tmp%d==0):
        e = tmp//d
        print(e)
        break
    k += 1
#  823816093931522017

# 快速求幂的算法
def  qpow(a,b,mod):
    ret  = 1
    while (b):
        if(b&1):
            ret = ret*a % mod
        a = a*a % mod
        b>>=1
    return ret

e = 823816093931522017
X = qpow(C,e,n)
print(X)
# 397418885977430817