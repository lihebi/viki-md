# Shell Script

用if比较两个字符串是否相等。

```sh
if [ `uname` != "Darwin" ]; then
  echo "true"
else
  echo "false"
fi
```

需要注意的问题：比较可以使用`!=`和`==`。
但是，两个字符串和操作符之间必须有空格！！简直坑爹。而且还不报错，直接认为表达式是true。
另外，`[`和后面的字符串之间也要有空格，否则shell识别不了`[`这个command。这个会报错。
