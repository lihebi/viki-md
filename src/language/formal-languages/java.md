# Java入门

## 一切都是对象

`String s;`
这里建立的不是对象，而是引用。这时向s发送消息会产生运行时错误。正确的做法是，创建一个引用的同时进行初始化：
`String s=‘asdf’;`
这是Java的一个特性：可以使用带引号的文本初始化字符串。有更一般的初始化方法，即`new`
`String s = new String(‘asdf’);`

# 基本类型

Java中的基本类型大小是固定的。全部都有正负，不存在`unsigned`。

｜ 基本类型 | 大小 | 包装器类型 |
| :---: | :---: | :---: |
| char | 16bit | Character |
| byte | 8bit | Byte |
| int | 32bit | Integer |
| short | 16bit | Short |
| long | 64bit | Long |
| float | 32bit | Float |
| double | 64bit | Double |
