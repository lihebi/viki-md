# CSS

## small tips

* margin可以是负的,padding不可以
* color: red !important;

## 选择器

* `element:nth-child(an + b)`: n start from 0, but 元素 from 1. 即第一个元素id是1

```
tr:nth-child(2n+1)
tr:nth-child(odd)
tr:nth-child(even)
span:nth-child(1) /* span的父节点的第一个孩子 */
span:nth-child(-n+3) /* 前三个 */
```

* `:root { xxx; }`: select the highest level node in DOM. For html, it is `<html>`
* `p:first-line`: the first line that is actually showed. first-letter select the first letter.
* `p:first-letter`
* `ul li:not(.active)`
* `div > p`: child selector. p必须是div的直接子。
* `span + span`: 直接相邻选择器。两个必须有同一parent，并且是紧密相邻。
* `div ~ p`: all p that are siblings of div


## 效果

### box-shadow

```
box-shadow: <offset-x> <offset-y> <blur-radius>? <spread-radius>? <color>?
```

```
-moz-
-webkit-
box-shadow:
```

examples:

```
box-shadow: 5px 5px 7px rgba(33,33,33,.7);
```

### gradients

#### Linear Gradients

```
background: linear-gradient(direction, color-stop1, color-stop2, ...);
```

browsers:

```
-webkit-linear-gradient(...)
   -moz-linear-gradient(...)
    -ms-linear-gradient(...)
     -o-linear-gradient(...)
        linear-gradient(...)
```

examples:

```
linear-gradient(red, green) /* top to bottom */
linear-gradient(left, red, green) /* left to right */
linear-gradient(left top, red green)
linear-gradient(180deg, red, green)
linear-gradient(left,rgba(255,0,0,0),rgba(255,0,0,1)) /* transparency */
linear-gradient(red, yellow 10%, green 20%) /* repeat */
```

#### Radial Gradients

```
background: radial-gradient(shape size at position, start-color, ..., last-color);
```

examples

```
radial-gradient(red, green)
radial-gradient(circle, red, green)
```


### transform

```
transform: none
transform: matrix(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
transform: translate(12px, 50%)
transform: translateX(2em)
transform: translateY(3in)
transform: scale(2, 0.5)
transform: scaleX(2)
transform: scaleY(0.5)
transform: rotate(0.5turn)
transform: skewX(30deg)
transform: skewY(1.07rad)
transform: matrix3d(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0)
transform: translate3d(12px, 50%, 3em)
transform: translateZ(2px)
transform: scale3d(2.5, 1.2, 0.3)
transform: scaleZ(0.3)
transform: rotate3d(1, 2.0, 3.0, 10deg)
transform: rotateX(10deg)
transform: rotateY(10deg)
transform: rotateZ(10deg)
transform: perspective(17px)

transform: translateX(10px) rotate(10deg) translateY(5px)
```

### transition

examples:

```
transition:  all 1s;
```

```
transition-property: background-color, color;
transition-duration: 1s;
transition-timing-function: ease-out;
```

```
transition-property: font-size;
transition-duration: 4s;
transition-delay: 2s;
```

## position

### static

正常

### relative

相对于正常。如果不设top,left,..，则无变化。
其引入两个特征：

* 可以使用`z-index`了。如果不指定`z-index`，它会出现在所有`static`元素的上方。
* 其子元素，若是`absolute`，其`absolute`的区域是此`relative`

### absolute

相对于一个`relative`或`absolute`的父节点。若无，则`hmtl`。
从`flow`中消失，不会影响也不会受其他元素影响。

###fixed

相对于`viewport`来说。

## display

* `inline`: default. `<span>`
* `block`: `<p>`
* `inline-block`: 是inline的，但是可以指定width,height

The inside of this block is formatted as block-level box. The element itself is formatted as inline-level box.

* `inline-table`: inline-level table
* `table`: behave like `<table>`
* `table-cell`: behave like `<td>`
* `none`
* `inherit`: inherit from parent

## Trouble Shooting

### inline-block item 之间会有默认的space，如何除去：

1. 把parent的font-size设为0
2. 把所有元素放到一行，中间没有空格
3. 把所有元素的换行用注释去掉
4. 把</div>的>放到下一行的开始

## Snippets

### file input button

```
<span class="btn btn-success fileinput-button">
<i class="glyphicon glyphicon-plus"></i>
<span>Add files...</span>
<input type="file" name="files[]" multiple>
</span>
```

```
.fileinput-button {
  position: relative;
  overflow: hidden;
}
.fileinput-button input {
  position: absolute;
  top: 0;
  right: 0;
  margin: 0;
  opacity: 0;
  -ms-filter: 'alpha(opacity=0)';
  font-size: 200px;
  direction: ltr;
  cursor: pointer;
}
```

### CSS Div中居中：

horizontal:

```
<div style=‘text-align: center’>
     <div style=‘margin: auto’>
     </div>
</div>
```

a text-aligned parent can align all the text of its children.
inline-block is treated as text; so use inline-block, don’t need margin:auto

vertical:

```
<div style=‘display: table’>
     <div style=‘display: inline-block; vertical-align: middle’>
     </div>
</div>
```

```css
.element {
  display: block;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}
```

### force text in one line

```css
p {
  white-space: nowrap;
  overflow: hidden;
}
```

### text indent

```css
p {
  text-indent: 2em;
}
```
