# String in Javascript

## Type

* primitive string: `'sss'`, `"sss"`, or `String("sss")` without `new`.
* string object: `new String("sss")`

```js
typeof('xx') // => "string"
typeof(new String('xx')) // => "object"
```

primitive string 调用方法时，自动转成 object。

### eval

```js
eval(new String("2+2")) // => string object "2+2"
eval("2+2") // => 4
var so = new String("2+2");
eval(so.toString()) // => 4
eval(so.valueOf()) // => 4
```

## Methods

all methods here are accessor, the initial string will not be changed.

* `String.prototype.charAt`
* `concat`
* `indexOf`
* `lastIndexOf`
* `match`: match a reg exp
* `replace(regexp|substr, newSubStr|function)`: find a match of regex, replace matched string with a new string

```js
data.replace(/\\"/g, '"');
data.replace(/\$([^$]+)\$/g, '<span class="katex">'+'$1'+'</span>');

var replacer = function(match, p) {
  return p.replace(...);
};
s.replace('/xxx/g', replacer);
```

See also: [replacer][replacer]
[replacer]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#Specifying_a_function_as_a_parameter

* `search`: search for a match on regex
* `slice(begin[, end])`: 切片返回. `end` can be negative, treated as `length+end`
* `split([seperator][, limit])`
  * if `seperator` is empty, return all characters.
  * `limit`: integer, specify a limit on the number of splits to be found
* `substr(start[, length])`
* `substring(indexA[, indexB])`
* `toLowerCase`
* `toUpperCase`
* `toString`
* `valueOf`: -> primitive value
* `trim`: trim white space at begin and end of string
