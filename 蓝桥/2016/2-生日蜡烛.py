'''
某君从某年开始每年都举办一次生日party，并且每次都要吹熄与年龄相
同根数的蜡烛。 现在算起来，他一共吹熄了236根蜡烛。

请问，他从多少岁开始过生日party的？ 请填写他开始过生日party的年龄数。
'''

age1 = 0
for age1 in range(100):
    sum = 0
    for i in range(age1,100):
        sum+=i
        if(sum==236):
            print("找到了age1："+str(age1))
            print("现在他年龄是："+str(i))
            break