n = 2021041820210418

xdata = []
#先求出n的系数
for i in range(1,n+1):
    if(n%i==0):
        if(i>n//i):
            break
        xdata.append(i)
        xdata.append(n//i)


ret = set()
length = len(xdata)

for i in range(length):
    L = xdata[i]
    for j in range(length):
        W = xdata[j]
        if(n%(L*W)==0):
            ret.add((L,W,n//(L*W))

print(len(ret))