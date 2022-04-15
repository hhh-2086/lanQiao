def merge(data,p,q,r):#p起点，r终点，q界限
    st = []
    p1 = p
    c = q+1#右部分
    while(p<=q and c<=r):
        while(p<=q and data[p]<=data[c]):
            st.append(data[p])
            p = p+1
        while(c<=r and data[c]<=data[p]):
            st.append(data[c])
            c = c+1
    #将余下的全部放入数组
    while(p<=q):
        st.append(data[p])
        p = p+1
    while(c<=r):
        st.append(data[c])
        c = c+1
    for i in st:#更新数组
        data[p1] = i
        p1 = p1+1
        
def merge_sort(data,p,r,n):#n记录递归次数
    n = n+1
    if(p<r):
        q = (p+r)//2
        n = merge_sort(data,p,q,n)#左部分排序
        n = merge_sort(data,q+1,r,n)#右部分排序
        merge(data,p,q,r)
        return n
    else:
        return n

#main()
data = [i for i in input().split()]
n = merge_sort(data,0,len(data)-1,0)
print(n)
for i in data:
    print(i,end=' ')

'''样例
48 38 65 97 76 13 27
输出
13
13 27 38 48 65 76 97
'''