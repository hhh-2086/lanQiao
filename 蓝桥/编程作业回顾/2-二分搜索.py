data = [int(i) for i in input().split()]
key = int(input())
for i in data:print(i,end=' ')
print()

low = 0
high = len(data)-1

def printall(h,l,data): #将数字转化为字符串输出
    for i in data[l:h+1]:
        print(i,end=' ')
    print()

while(low<=high):
    mid = (low+high)//2
    if(key == data[mid]):
        print(mid+1)    #输出所在位置
        break

    elif(key<data[low]):#比最小值还小
        print(0)
        break
    elif(key>data[high]):#比最大值还大
        print(0)
        break

    elif(key>data[mid]):
        low = mid+1
        printall(high,low,data)
    else:
        high = mid-1
        printall(high,low,data)
'''【样例1输入】
 15 17 18 22 35 51 60 88 90 100
 18
【样例1输出】 
15 17 18 22 35 51 60 88 90 100
15 17 18 22
18 22
3#对应的下标，从1开始
【样例3输入】
15 17 18 22 35 51 60 88 90 100
70
【样例3输出】
15 17 18 22 35 51 60 88 90 100
51 60 88 90 100
51 60
0#不存在
【样例3说明】
 输入：10个有序整数，以空格分隔。要寻找的特定元素为70。
 输出：第一至第三行为三次搜索的所在范围内的整数。第四行为0，表示特定元素70在有序数组不存在。
 '''