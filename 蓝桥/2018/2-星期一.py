'''
整个20世纪（1901年1月1日至2000年12月31日之间），一共有多少个星期一？
(不要告诉我你不知道今天是星期几)

注意：需要提交的只是一个整数，不要填写任何多余的内容或说明文字。
'''
# 2000.12.31 是周日
# 计算所有的天数。以及考虑闰年
# 答案：5217
from cgitb import reset


def findRun(year):
    if(year%400==0):
        return 1
    if(year%4==0 and year%100!=0):
        return 1
    return 0

flag = 0
for i in range(1901,2001):
    if(findRun(i)):
        flag+=1
print(flag)
# 25年闰年
# 一共100年
allDay = flag+365*100
result = allDay//7
result1 = allDay%7
print(result)
print(result1)
# 最后是5217余6。1901.1.1正好是周一
# 因为是从2000年12.31倒着向前计算的。所以向下取整。