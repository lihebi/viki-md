# CORS

Cross Origin Resource Sharing

## Out Lines

CORS works by adding new HTTP headers
that allow servers to describe the set of origins
that are permitted to read that information using a web browser.

Additionally, for HTTP methods other then GET,
or for POST usage with certain MIME types,
Browsers preflight the request, soliciting supported methods from server with an HTTP OPTIONS request,
then, upon approval from the server,
sending the actual request with actual HTTP request method.

CORS在HTTP header中加入新的项目。
对于不是GET的请求，或者用于特定MIME的POST，
浏览器预处理req(preflight)，先发一个OPTIONS，得到服务器允许后，再发送真的请求。

## 请求类型

### 简单请求

如果一个请求：

* 只使用GET,HEAD,POST。
POST如果用来send data的话，
其Content-Type是`application/x-www-form-urlencoded`,`multipart/form-data`, or `text/plain`
* **而且**没有其他自定义的header

这时候，不需要在客户端做任何事情，只需要服务器返回response时，加入`Access-Control-Allow-Origin: *`，
或者`Access-Control-Allow-Origin: http://lihebi.com`，其中`http://lihebi.com`是在request中的Origin项。

### Preflighted requests

如果一个请求：

* 使用除了GET,HEAD,POST外的别的method，或者POST传了data，却使用不是上述三种Content-Type
* **或者**set custom headers

关于OPTIONS:

OPTIONS is an HTTP/1.1 method that is used to determine further infomation from servers.
It is an **idempotent** method(幂等),meaning that it can't be used to change the resource.

javascript snippet:

```
var invocation = new XMLHttpRequest();
var url = 'http://bar.other/resources/post-here/';
var body = '<?xml version="1.0"?><person><name>Alice</name></person>';

function callOtherDomain() {
  invocation.open('POST', url, true);
  invocation.setRequestHeader('X-PINGOTHER', 'pingpong');
  invocation.setRequestHeader('Content-Type', 'application/xml');
  invocation.onreadystatechange = handler;
  invocation.send(body);
}
```

OPTIONS:

```
Origin: http://foo.example
Access-Control-Request-Method: POST # when actual request is sent, it will be a POST method
Access-Control-Request-Headers: X-PINGOTHER # when actual request is sent, it will have custom header X-PINGOTHER
```

Response for OPTIONS:

```
Access-Control-Allow-Origin: http://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER # can also be a list seperated by comma
# how long the response to the preflight request can be cached for without sending another preflight request.
# 1728000 seconds is 20 days.
Access-Control-Max-Age: 1728000
Vary: Accept-Encoding, Origin
```

Then will be the POST request:

```
POST /resources/post-here/
X-PINGOTHER: pingpong
...

<?xml ....
```

Then response:

```
Access-Control-Allow-Origin: http://foo.example
Vary: Accept-Encoding, Origin
```

### Requests with credentials

bar.other要设置cookie

javascript

```
var invocation = new XMLHttpRequest();
var url = 'http://bar.other/resources/credentialed-content/';
function callOtherDomain() {
  invocation.open('GET', url, true);
  invocation.withCredentials = true; # key
  invocation.onreadystatechange = handler;
  invocation.send();
}
```

这个请求是个简单请求，不会preflight. 但是这时候的response要满足两个条件

* Access-Control-Allow-Origin: http://foo.example, 而且不能用`*`
* Access-Control-Alow-Credentials: true

注意到，Access-Control-Allow-Origin可以使用`*`，但是一旦使用了具体domain，一定要同时将Origin包括在Vary中，
以告诉客户端，server response will differ based on the Origin request header.

```
Vary: Accept-Encoding, Origin
```


