# adblock
## 基础过滤器

可以直接加入`http://example.com/ads/banner123.gif`。
可以使用通配符`http://example.com/ads/banner*.gif`。

## 例外

如果不想屏蔽`http://example.com/advice.html`，可以使用`@@advice`。
例外中也可以使用通配符和正则。
如果例外是由`http`或者`https`开始的（可以optionally有一个`|`），那么会把整个页面作为例外。例如：
`@@|http://example.com`会使`adblock`在整个页面上失效。

## 明确的前后

adblock默认会认为每个规则前后都有通配符。所以，`ad`和`*ad*`没有任何区别。
为了明确前后，可以加`|`。
`swf|`说明在swf后没有任何东西了。
`|http://xxx`说明在前面没有了。
`||example.com/banner.gif`可以屏蔽`http://example.com/banner.gif`,`https://example.com/banner.gif`,`http://www.example.com/banner.gif`。

## 分隔符

分隔符：除了字母，数字，`_-.%`以外的所有字符。包括一个地址的结束。例子：
为了屏蔽`http://example.com/`和`http://example.com:8000/`但是保留`http://example.com.ar/`，使用`http://example.com^`

## 注释

以`!`开头。

# 隐藏内容

有些广告是在html中的，只能隐藏。例如

```html
<div class="textad">
  Cheapest tofu, only here and now!
</div>
<div id="sponsorad">
  Really cheap tofu, click here!
</div>
<textad>
  Only here you get the best tofu!
</textad>
```

使用`##div.textad`来隐藏`div`元素中的`textad`类。`##`是隐藏的标识符。
使用`##div#sponsorad`隐藏特定`id`
可以使用通配符指定所有元素`##*#sponsorad`
或者使用元素only`##textad`

## 只应用于特定网站

`example.com##*.sponsor`对`http://example.com/`和`http://something.example.com/`生效。
同时指定多个域名：`domain1.example,domain2.example,domain3.example##*.sponsor`
` ~example.com##*.sponsor`将会应用于**除了**`example.com`以外的所有域名。
最后，隐藏内容所使用的域名必须是域名本身。

## 使用属性选择器

如果一个广告没有id,可以使用属性。
`##table[width="80%"]``width`是`80%`的`table`。
` ##div[title*="adv"]`所有div，其`title`属性包括字符串`adv`。
`##div[title^="adv"][title$="ert"]`div中title以`adv`开始，以`ert`结束。同时这也说明可以同时使用多个属性选择器。

## 例外

`##div.textad`和`example.com#@#div.textad`等价于
`~example.com##div.textad`
