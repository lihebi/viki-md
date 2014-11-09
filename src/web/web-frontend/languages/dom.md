# DOM

## window

* `window.innerHeight`: height of the content area of the browser, 自动去掉inspector
* `window.innerWidth`
* `window.location`: object used to get/set location or currentURL

## document

`window.document`

### Attributes

* `document.contentType`: "text/html"
* `charset`: "UTF-8"
* `documentURI`: "http://xxx/xxx/xxx"
* `styleSheets`: [obj1, obj2, ...]
* `children`: [<html>xxx</html>]
* `body`: body element. <body>...</body>
* `cookie`: a semicolon-separated list of cookies for this document. or used to set a single cookie.
* `domain`: "viki.lihebi.com"
* `forms`: a list of form elements
* `head`: head element
* `images`: a list of images
* `links`: all links
* `location`: same as `window.location`
* `scripts`: all script elements
* `title`: title
* `URL`

### Methods

* `document.createElement(tagname)`
* `getElementByClassName(className)`
* `getElementByTagName(s)`
* `getElementById(s)`
* `getElementByName(s)`
* `querySelector(s)`: first element
* `querySelectorAll(s)`: all elements
* `hasFocus()`: true if focus located anywhere in this document

## navigator

* `navigator.userAgent`: "Mozilla/5.0..."
