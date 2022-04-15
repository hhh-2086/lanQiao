data = {}  #标记每一个字符消耗的个数

for i in range(10):
    data.update({i:0})

print(data)
num = 1
flag = 1
while(True):
    s = str(num)
    
    for i in range(len(s)):
        data[int(s[i])]+=1
        if(data[int(s[i])]>=2021):
            flag  = 0
            break
    if(flag==0):
        break
    num += 1

print(num)
print(data)
