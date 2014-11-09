# Array in Javascript

## Mutator Methods

These methods will change the original array.

* `Array.prototype.pop()`: pop last element
* `push`: push to last
* `reverse`: reverse order
* `shift`: remove and return first element
* `sort`
* `splice(index, howMany[, ele1[, ele2[, ...]]])`

from `index`, remove `howMany` elements, add `ele1, ele2, ..., eleN`.

* `unshift(ele1[, ele2[, ...]])`: 在前面加一个或多个。

## Accessor Methods

* `Array.prototype.concat`

```js
var num1 = [1,2,3];
var num2 = [4,5,6];
var num3 = [7,8,9];
num1.concat(num2, num3, 1, 2) // => [1,2,3,4,5,6,7,8,9,1,2]
```

* `join([seperator=','])`: join elements into a string. default separator is comma
* `indexOf`
* `lastIndexOf`

## Iteration Methods

If not mentioned, callback is `cb(value, index, array)`.

* `Array.prototype.forEach(cb[, thisArg])`: no way to break or stop a forEach loop
* `every(cb[, thisArg])`: 对array的每一个元素执行cb，若回false，则立马返回false。若所有都是true，返回true。
* `some(cb[, thisArg])`: 对array的每一个元素执行cb，若回true，则立马返回true。若素有都是false，返回false。
* `filter(cb[, thisArg])`: create a new array with all elements that pass cb.
* `map(cb[, thisArg])`: create a new array with results of calling cb on all elements
* `reduce(cb[, initialValue])`

`cb(previousValue, currentValue, index, array)`

previousValue 是上一次cb的result或者initialValue.

* `reduceRight(cb[, initialValue])`
