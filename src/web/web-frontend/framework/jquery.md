# JQuery

## Ajax

```
$.ajax(url, {
  type: 'POST' // 注意不是method
  })
```

## Selector

each function

```
$('li').each(function(index)) {
  $(this).text();
};
```

## jquery to dom

```
$('#test').get()[0]
// same as
document.getElementById('test')
```


```js
$(window).height()
$(window).width()

$(document).width()
$(document).height()
```
