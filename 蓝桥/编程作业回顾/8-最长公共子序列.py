X = input().split()
Y = input().split()
#len(X)+1行，len(Y)+1列
c =[ [0 for i in range(len(Y)+1)] for j in range(len(X)+1)]
b = [ ['' for i in range(len(Y))] for j in range(len(X))]
def L(X,Y,m,n,c,b):
    for i in range(m):#一行一行初始化
        for j in range(n):
            if(X[i]==Y[j]):
                c[i+1][j+1] = c[i][j]+1
                b[i][j] = 'q'#表示左上角
            elif(c[i][j+1]>=c[i+1][j]):
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = 'w'#表示上方
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = 'a'#表示左方

L(X,Y,len(X),len(Y),c,b)
print(c[len(X)][len(Y)])
result = []
m = len(X)
n = len(Y)
while(c[m][n]!=0):
    if(b[m-1][n-1]=='q'):
        m = m-1
        n =n-1
        result.append(X[m])
    elif(b[m-1][n-1]=='w'):
        m = m-1
    else:
        n = n-1

for i in range(len(result)-1,-1,-1):
    print(result[i],end='')

if(len(result)==0):
    print("None")#输出空序

'''
A B C B D A B
B D C A B A
'''