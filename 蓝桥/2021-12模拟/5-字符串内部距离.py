'''
两个字母之间的距离定义为它们在字母表中位置的距离。
例如A和C的距离为2，L和Q的距离为5。对于一个字符串，我们称字符串中两两字符之间的距离之和为字符串的内部距离。

例如：ZOO的内部距离为22，其中Z和O的距离为11。

请问，LANQIAO的内部距离是多少？
'''
# 162
s = 'LANQIAO'
re = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        re+=abs(ord(s[i])-ord(s[j]))

print(re)
# 162