Paper Review: Google File System
================================

观察到的现象
----------

* component failure是正常的，而不是异常
* 文件很大，有几个GB很常见
* 大多数文件的修改是添加(append)而不是覆盖(random write)。数据是流。
* 把应用和FS API一起设计，更灵活，可以根据我的需求去设计API.

Design
-------

一个集群中，有1个master和很多chunk server。对一个大文件，把它分成很多chunk去存放。
所有的chunk都存在chunk server上，是一个普通的linux文件。linux会像对待普通文件一样对它用缓存。
chunk的典型三小是64M。这么三的好处是我很多读写很可能都是在这同一个chunk中的。
另一个好处是master中的metadata就会比较少。
也有问题，容易造成内存碎片。但是可以用lazy space allocation来解决。
另一个缺点：一个文件可能就在一个chunk里，但是它可能很hot，这样就有很多client去请求他，造成单点大负载。
解决办法是对这种chunk，提高其replicate factor.
一个long term solution是，这种情况下，client可以临近的client去读。
每个chunk典型的是replica三份。
chunk在其创建时就会被命名一个不变的全局唯一的名字，叫chunk handle。

一个典型的read过程：
client将要读的文件名和读取的chunk index（自己算，因为知道每个chunk的size）发给master。
master返回对应的chunk handle和replica的位置。client将这些信息缓存。
然后，client向一个replica（可能是closet的）发handle和byte range进行读写。
直到cache过期或者file reopen，client和master都不需要再次通信。

master上存metadata。有3个东西：file and chunk namespace, file到chunk的mapping，没一个replica的位置。
前两个以增量的形式保存在log里，以便恢复。第三个不存，只在memory里。在master启动时从chunk server处收集。
然后通过心跳包来进行同步更新。
log非常重要，因此
