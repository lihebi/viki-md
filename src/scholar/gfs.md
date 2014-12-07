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

### 集群的架构
一个集群中，有1个master和很多chunk server。对一个大文件，把它分成很多chunk去存放。
所有的chunk都存在chunk server上，是一个普通的linux文件。linux会像对待普通文件一样对它用缓存。
chunk的典型三小是64M。这么大的好处是我很多读写很可能都是在这同一个chunk中的。
另一个好处是master中的metadata就会比较少。
也有问题，容易造成内存碎片。但是可以用lazy space allocation来解决。
另一个缺点：一个文件可能就在一个chunk里，但是它可能很hot，这样就有很多client去请求他，造成单点大负载。
解决办法是对这种chunk，提高其replicate factor.
一个long term solution是，这种情况下，client可以临近的client去读。
每个chunk典型的是replica三份。
chunk在其创建时就会被命名一个不变的全局唯一的名字，叫chunk handle。

### 一个典型的read过程：
client将要读的文件名和读取的chunk index（自己算，因为知道每个chunk的size）发给master。
master返回对应的chunk handle和replica的位置。client将这些信息缓存。
然后，client向一个replica（可能是closet的）发handle和byte range进行读写。
直到cache过期或者file reopen，client和master都不需要再次通信。

### MetaData
master上存metadata。有3个东西：file and chunk namespace, file到chunk的mapping，没一个replica的位置。
前两个以增量的形式保存在log里，以便恢复。第三个不存，只在memory里。在master启动时从chunk server处收集。
然后通过心跳包来进行同步更新。
log非常重要，因此我们要replica多份。在没有完全flush(both locally and remotely)之前对client是不可见的。

为了恢复状态，直接replay log就行了。但是log很大就不好了。
因此，当log达到一定size时，換一个log文件，并新开一个线程去checkpoint換文件之前的所有状态。
这个过各程要1分钟。
checkpoint要B+树，直接拷贝到内存中就可以使用。然后replay之后的log就行了。
就算在制作checkpoint的过程中跪掉了也无所谓，少而恢复时会跳过不完整的checkpoint.

### 文件状态

* consistent: a file region is consistent if all clients will see the same data
* defined: a region is defined after a data mutation if
it is consistent and clients will see the mutation.

如下表：

|   | Write | record append(atom write) |
| :------------- | :------------- | :--- |
| Serial success | defined | consistent but undefined | defined interspersed with inconsistent |
| concurrent success | same as above |
| faliure | inconsistent | inconsistent |

对于serial success, GSF保证其是defined：
1. mutations apply to chunks in the same order
2. use chunk version number to detect stale
Stale replica never involve 一个新的mutation，也不会被master将地址发给client.
但是client有cache，也会读过去。这只能用缓在时间来控制。同时file reopen也会控制。
另外，由于绝大多数的mutation都是append，所以要从replica读到没有添加的信息，只会返回EOF。
这样client自己就知道要向master要新的緩存。

一个failure在何种情况下都会destroy data。
GSF通过regular shakehands between master and chunkserver来检测到(by checksum)。
然后用别的replica恢复。只有当所有replicca lost时才会lost.
这时候client会收到明确的出错信息而不是错误数据。

### control flow and data flow

master将某一个replica标记为primary，然后给它一个lease，60秒时效。

1. client向master要哪一个replica有lease。
2. master告诉它，并且告诉它其佘的replica.
3. client以任意order推送data到所有replica上。replia缓存它们。
4. 当所有replica都confirm它们收到了，client向primary发write request.
Primary对所有mutation排序。
5. primary将排序发给所有其佘replica。
6. 所有replica回复primary success
7. primary回复client。
