data = [int(i)for i in input().split()]

def printall(data): #将数字转化为字符串输出
    for i in data:print(i,end=' ')
    print()

def perm(data,k,m):
    if(k==m):
        printall(data)
    else:
        for i in range(k,m+1):
            data[k],data[i] = data[i],data[k]#交换
            perm(data,k+1,m)
            data[k],data[i] = data[i],data[k]  #交换

perm(data,0,len(data)-1)