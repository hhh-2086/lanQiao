'''
编程题
现在时间是a点b分，请问t分钟后，是几点几分？

【输入格式】

输入的第一行包含一个整数a。

第二行包含一个整数b。

第三行包含一个整数t。

【输出格式】

输出第一行包含一个整数，表示结果是几点。

第二行包含一个整数，表示结果是几分。
【样例输入】
3
20
165

【样例输出】
6
5
'''
a = int(input())
b = int(input())
# a点b分
t = int(input())

tt = 59-b
if(t<=tt): #分钟不会进位
    b = b+t
    print(a)
    print(b)
elif((t-tt)/60<0): #分钟进位，时钟不进位
    a += (t-tt)//60
    b = 60-(t-tt)//60
else:#时钟进位
    a = (a+(t-tt)//60)%24
    b = 60-(t-tt)//60

print(a)
print(b)