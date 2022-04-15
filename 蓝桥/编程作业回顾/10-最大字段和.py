a = [int(i) for i in input().split()]
a.insert(0,0)
n = len(a)-1
sum = 0
b = 0
l,r = 1,1
for i in range(1,n+1):
    if(b>0):
        b = b+a[i]
    else:
        b = a[i]
        if(b>0):
            l = i
    if(b>sum):
        sum = b
        r = i

print(sum)
print(l)
print(r)