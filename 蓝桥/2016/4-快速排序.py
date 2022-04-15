'''
以下代码可以从数组a[]中找出第k小的元素。
它使用了类似快速排序中的分治算法，期望时间复杂度是O(N)的。
请仔细阅读分析源码，填写划线部分缺失的内容。
#include <stdio.h>


int quick_select(int a[], int l, int r, int k) {undefined
    int p = rand() % (r - l + 1) + l;
    int x = a[p];
    {int t = a[p]; a[p] = a[r]; a[r] = t;}
    int i = l, j = r;
    while(i < j) {undefined
        while(i < j && a[i] < x) i++;
        if(i < j) {undefined
            a[j] = a[i];
            j--;
        }
        while(i < j && a[j] > x) j--;
        if(i < j) {undefined
            a[i] = a[j];
            i++;
        }
    }
    a[i] = x;
    p = i;
    if(i - l + 1 == k) return a[i];
    if(i - l + 1 < k) return quick_select( ____(a,p+1,r,k-p  +l-1)_________________________ ); //填空
    else return quick_select(a, l, i - 1, k);
}
    
int main()
{undefined
    int a[] = {1, 4, 2, 8, 5, 7, 23, 58, 16, 27, 55, 13, 26, 24, 12};
    printf("%d\n", quick_select(a, 0, 14, 5));
    return 0;
}
'''