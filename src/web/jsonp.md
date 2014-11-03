# JSONP

html:

```
<script>var mycallback = function(data){ alert(data);};</script>
<script src="http://a.com/api?callback=mycallback></script>
```

server返回的script中，插入了我们的callback函数名，将数据放入函数参数中。
这样，我们运行加载的脚本后，便调用了我们的函数，而使用载入的数据。

基于：script标签的evaluation不考虑cross domain.
