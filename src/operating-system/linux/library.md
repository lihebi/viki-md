# Library

Static Library .a
==============

### 生成

```
cc -Wall -c a1.c a2.c
ar -cvq liba.a a1.o a2.o
```

### list files in Static Library

```
ar -t liba.a
```

### 使用

```
cc -o out prog.c liba.a
cc -o out prog.c -L/path/to/library -la
```

### 例子

a1.c

```
void func1(int *i) {
  *i = 5;
}
```

a2.c

```
void func2(int *i) {
  *i = 100;
}
```

prog.c

```
#include <stdio.h>
void func1(int*);
void func2(int*);

int main() {
  int x;
  func1(&x);
  return 0;
}
```

Dynamic Library(Shared Library): .so
=====================================

### 生成

```
gcc -Wall -fPIC -c *.c
gcc -shared -W1,-soname,liba.so.1 -o liba.so.1.0 *.o
```

move to regular location and create symbol links

```
mv liba.so.1.0 /opt/lib
ln -sf /opt/lib/liba.so.1.0 /opt/lib/liba.so.1
ln -sf /opt/lib/liba.so.1.0 /opt/lib/liba.so
```

Compiler Option的说明：

* `-Wall`: include all warnings
* `-fPIC`: 产生与位置无关的代码。shared library必须。
* `-shared`: Produce a shared object which can then be linked with other objects to form an executable.

Symbol Link的作用

* `/opt/lib/liba.so`: allow `-la` to work.
* `/opt/lib/liba.so.1`: allow run time binding to work.

### 使用

```
gcc -Wall -I/path/to/include-files -L/path/to/libraries prog.c -la
```

并不会在编译时就包含进去，而是在运行时动态连接。

### List dependencies

```
ldd out
```

### Path

#### ld.so.conf

`/etc/ld.so.conf`这个文件包含所有library搜索路径。每行一个。
直接修改，然后运行

```
sudo ldconfig
```

来更新`/etc/ld.so.cache`

也可以使用

```
sudo ldconfig -f filename
```

来指定一个文件。

#### ldconfig -n

```
ldconfig -n /opt/lib
```

这样会暂时增加此路径，但是重启后会消失。比较适合调试用。

#### LD_LIBRARY_PATH

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib
```

放在`.shrc`中的写法一般是：

```sh
if [ -d /opt/lib ];
then
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib
fi

export LD_LIBRARY_PATH
```

#### 直接在编译选项里指定 -L -I

Library Info
================

```
ar tf x.a
nm x.a
readelf -s x.so
```

C++和C互相调用
============

为了C++可以调用C的库，需要在相应的头文件中加入

```c
#ifdef __cplusplus
extern "C" {
#endif

void func1(int*);
void func2(int*);

#ifdef __cplusplus
}
#endif
```
