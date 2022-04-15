'''
填空题

请问有多少个序列满足下面的条件：

1.序列的长度为5。

2.序列中的每个数都是1到10之间的整数。

3.序列中后面的数大于等于前面的数。
'''
# 2002

result = set()
r = 0
for i1 in range(1,11):
    for i2 in range(i1,11):
        for i3 in range(i2,11):
            for i4 in range(i3,11):
                for i5 in range(i4,11):
                    r +=1

print(r)
# 2002