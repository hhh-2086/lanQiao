'''
给定数列1, 1, 1, 3, 5, 9, 17, …，从第4 项开始，每项都是前3 项的和。求
第20190324 项的最后4 位数字。
'''
data = [1, 1, 1]
for i in range(3,20190324):
    data.append((data[0]+data[1]+data[2])%10000)#只关注最后四位数。求和的特点
    data.pop(0)

print(data)
# 4659
