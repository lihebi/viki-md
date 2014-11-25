# Maximum Product Subarray

[Maximum Product Subarray]
(https://oj.leetcode.com/problems/maximum-product-subarray/)
`medium`


## Good Solution

Dynamic Programming.

f(k) = Largest product subarray, from index 0 up to k INCLUDING k.

g(k) = Smallest product subarray, from index 0 up to k INCLUDING k.

$f(k) = max( f(k-1) * A[k], A[k], g(k-1) * A[k] )$

$g(k) = min( g(k-1) * A[k], A[k], f(k-1) * A[k] )$

再从所有f(k)中选出最大值。


## My Solution

1. 对数组以0分段
2. 对于每组，找到最左和最右的负数
3. 算出这两个负数中间的product
4. 中间若大于0,则返回整个array's product
5. 若小于0,则比较`start to r` and `l to end`

```cpp
class Solution {
  public:
    int maxProduct(int A[], int n) {
      int x=0;
      int result=A[0];
      for (int i=0;i<n;i++) {
        if (A[i] == 0) {
          // wrong in case [-1,0,-2]
          result = result>0?result:0;
          /*
           *this case i=x
           */
          if (A[x]==0) {
            result = result>0?result:0;
            x++;
          }
          /*
           *parse a none empty none 0 sub array
           */
          else {
            int tmp = subMax(A, x, i-1);
            if (tmp>result) result = tmp;
            x = i+1;
          }
        }
      }
      // the last one is not 0, do subMax one more time!!!!! TODO add to common problem
      if (A[n-1]!=0) { // n-1!!!!! TODO add to common problem
        int tmp = subMax(A,x,n-1);
        if (tmp>result) {
          result = tmp;
        }
      }
      // I forgot to return.....
      return result;
    }
  private:
    int subMax(int A[], int x, int y) {
      int l=y+1,r=x-1;
      int i;
      // in case Only one number and it's negative
      if (x==y) return A[x];
      /*
       *get left most and right most negative
       */
      for(i=x; i<=y;i++) {
        if (A[i]<0) {
          if (l>i) l=i;
          if (r<i) r=i;
        }
      }
      /*
       *no negative found
       */
      if (r==x-1) {
        int tmp=1;
        for (i=x;i<=y;i++) {
          tmp *= A[i];
        }
        return tmp;
      }
      /*
       *1 negative found
       */
      if (l==r) {
        int tmp1=1,tmp2=1;
        for (i=x;i<l;i++) {
          tmp1 *= A[i];
        }
        for (i=l+1;i<=y;i++) {
          tmp2 *= A[i];
        }
        return tmp1>tmp2?tmp1:tmp2;
      }
      /*
       *multiple negative found
       */
      int mid = 1;
      for (i=l+1;i<r;i++) {
        mid *= A[i];
      }
      if (mid>0) {
        for (i=x;i<=l;i++) {
          mid *= A[i];
        }
        for (i=r;i<=y;i++) {
          mid *= A[i];
        }
        return mid;
      }
      int tmp1=mid,tmp2=mid;
      for (i=x;i<=l;i++) {
        tmp1 *= A[i];
      }
      for (i=r;i<=y;i++) {
        tmp2 *= A[i];
      }
      return tmp1>tmp2?tmp1:tmp2;
    }
};
```
