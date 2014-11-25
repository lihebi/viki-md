# Find Minimum in Rotated Sorted Array

[Find Minimum in Rotated Sorted Array](https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
`medium`

## My Solution

```cpp
class Solution {
public:
    int findMin(vector<int> &num) {
        int x,y,tmp;
        x=0;y=num.size()-1;
        while(x!=y) {
            tmp = ceil((x+y) * 0.5); // can not use /2, because it will convert to int, which is round(not ceil, 3.5=>3).
            if (tmp == y) return num[x]>num[y]?num[y]:num[x]; // x and y are near each other
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
