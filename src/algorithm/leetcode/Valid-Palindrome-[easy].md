# Valid Palindrome


[Palindrome](https://oj.leetcode.com/problems/valid-palindrome/) `easy`

## My Solution:

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0, end = s.size()-1;
        while (start < end) {
            if (!isalnum(s[start])) // built-in function!!
                start++;
            else if (!isalnum(s[end])) // built-in function
                end--;
            else if (tolower(s[start]) != tolower(s[end])) // built-in function
                return false;
            else {
                start ++;
                end --;
            }
        }
        return true;
    }
};
```

But the following will cause Time out:

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int length = s.length();
        for(int i=0, j=length-1;i<=j;) {
            while(i<length && !check(s,i)) { // check if i>length. Crucial
                i++;
            }
            while(j>=0 && !check(s,j)) {
                j--;
            }
            if (i>j) break; // Crucial
            if (!caseEqual(s[i], s[j])) return false;
            i++;
            j--;
        }
        return true;
    }
private:
    bool check(string s, int i) {
        return (s[i]>='a' && s[i]<='z') || (s[i]>='A' && s[i]<='Z') || (s[i]>='0'&&s[i]<='9'); // '0' instead of 0
    }
    bool caseEqual(char a, char b) {
        return a==b || a-b==32 || b-a==32;
    }
};
```
