'''
//答案：x&(x+1)
//下面的代码把一个整数的二进制表示的最右边的连续的1全部变成0 如果最后一位是0，则原数字保持不变
#include <stdio.h>
 
void f(int x)
{
    int i;
    for(i=0; i<32; i++) printf("%d", (x>>(31-i))&1);
    printf("....");
    
    x =  _______________________;
    
    for(i=0; i<32; i++) printf("%d", (x>>(31-i))&1);
    printf("\n");    
}
 
int main()
{
    f(128+64+2);  //194
    f(128+64+15); //207
    f(128+64+1);  //193
    
    return 0;
}
'''