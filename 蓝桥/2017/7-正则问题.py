'''
考虑一种简单的正则表达式： 只由 x ( ) | 组成的正则表达式。  小明想求出这个正则表达式能接受的最长字符串的长度。  例如 ((xx|xxx)x|(x|xx))xx 能接受的最长字符串是： xxxxxx，长度是6

输入：  ((xx|xxx)x|(x|xx))xx 

程序应该输出： 6
'''

s = input()
length = len(s)
def outMax(index):
    m = 0
    ret = 0 #临时变量

    while(index<length):
        if(s[index] == '('):
            index += 1
            out,index =  outMax(index)
            ret+=out
        elif(s[index]=='x'):
            index += 1
            ret += 1
        elif(s[index]=='|'):
            index += 1
            m = max(m,ret) #保留一次最大值。也可能只有一个有值，另一个是0
            ret = 0
        elif(s[index]==')'):
            index += 1
            m = max(m,ret)
            return m,index
    m = max(m,ret)
    return m,index

re,index = outMax(0)
print(re)