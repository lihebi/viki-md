# Min Stack

好久不写c程序了，语法忘了一半。记录一下basic syntax吧。

[MinStack](https://oj.leetcode.com/problems/min-stack/) `easy`

算法: use an extra stack to store min values.
When push, if it is smaller or equal to current min, push.
When pop, if it is equal to current min, pop.

```cpp
class MinStack {
public:
    void push(int x) {
        s.push(x);
        if (ms.empty() || x<=ms.top()) {
            ms.push(x);
        }
    }
    void pop() {
        int tmp = s.top();
        s.pop();
        if (tmp==ms.top()) {
            ms.pop();
        }
    }
    int top() {
        return s.top();
    }
    int getMin() {
        return ms.top();
    }
private:
    std::stack<int> s;
    std::stack<int> ms;
};
```

也有更简单的方法，每次不比较，直接push min，每次也直接pop min。但是，
不能每次都push min，会导致Memory Exceed. 但是Java同样算法就不会，太特么坑了。
