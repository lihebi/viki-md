# Find Minimum in Rotated Sorted Array II

[Find Minimum in Rotated Sorted Array II]
(https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
`hard`

## My Solution

只对初始情况分析即可，若v[x]=v[y],则将x++，直到不一样。
其余不变。

```cpp
class Solution {
public:
    int findMin(vector<int> &num) {
        int x,y,tmp;
        x=0;y=num.size()-1;
        if (num[x]==num[y]) {
            tmp = x;
            // x++; // Wrong if only [1] is inputted.
            while(num[x]==num[tmp]) {
                tmp=x;x++;
                  if (x>y) return num[y];
            }
        }
        if (num[x]<num[y]) return num[x];
        while(x!=y) {
            tmp = ceil((x+y) * 0.5);
            if (tmp == y) return num[x]>num[y]?num[y]:num[x];
            if (num[tmp] > num[y]) {
                x = tmp;
            } else {
                y = tmp;
            }
        }
        return num[x];
    }
};
```
