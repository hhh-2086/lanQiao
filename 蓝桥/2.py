
ret = set()
def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

for x1 in range(20):
    for y1 in range(21):
        for x2 in range(20):
            for y2 in range(21):
                a = y2-y1
                b = x1-x2
                c = y1*x2-x1*y2

                if(a==b and b==c):
                    continue
                if(a==0 or b==0):
                    continue
                k = gcd(a,b)
                k = gcd(k,c)

                aa = a//k
                bb = b//k
                cc = c//k
                ret.add((aa,bb,cc))

print(len(ret))
#print(ret)
#40216
#加上没有被计入的
#但是最终没有计入斜率=0的直线,以及没有斜率的直线
