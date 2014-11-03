# Base64

## Concept

将非ASCII字符编成ASCII字符。有64个基本的ASCII码。

1. 把要编码的内容，每3个字节放入一组，共24bit。
2. 将其再分为4组，每组6个。$2^6=64$
3. 每组在前面补两个0，组成字节。共4个字节。
4. 若总字节数不是3的倍数，在最后加1或2个`=`

## JS

encoding:

```
var encodedData = window.btoa('...');
```

decoding:

```
var decodedData = window.atob('...');
```

### 中文乱码

对于所有的Unicode都存在这个问题。

```
decodedData = decodeURIComponent(escape(window.atob(encodedData)));
```
