NP Problems
==============

说明：证明中都省略了**证明构造能在P内完成**

CLIQUE
--------------

* `英文定义`:
A clique in an undirected graph $G=(V,E)$ is a subset $V' \subseteq V$ of vertices,
each pair of which is connected by an edge in E.
* `中文定义`: 首先，clique是无向图G中的一个子集。这个子集中的所有点在G中是两两相连的。
也就是说，clique is a complete subgraph of G.
* `CLIQUE problem`: 我们定义`size of clique`为该子集中的顶点个数。
那么`clique problem`就是要找到最大的CLIQUE.
* `decision problem`: 对于一个图G，是否存在size为k的clique.
* `正式定义`: CLIQUE = { $<G,k>$: G is a graph containing a clique of size k}

### 证明CLIQUE是NP-complete

* `证明NP`: 对于一个图$G=(V,E)$，我们用$V' \subseteq V$来表示一个certificate。
为了验证$V'$是否是clique，我们检查每一个pair $u,v \in V'$，其边$(u,v) \in E$.
可以在Polynomial Time内实现。

* `证明NP-Hard`. 证明$3-CNF-SAT \le_P CLIQUE$.

* `构造`：对于任何一个3-CNF-SAT，设其有k个clause,每个clause有3个变量。也就是：
$\phi = (x_1 \vee x_2 \vee \neg x_3) \wedge \ldots$
把所有的变量（允许重复）都放入G中。
对与每组中三个变量的每一个，将其与其余所有组的所有变量连接，除非他们互补（$x$ and $\neg x$）。

* `=>`: 如果$\phi$有一个satisfying assignment，那么：
其中的每一组至少有一个变量是1.把这些变量全部取出来当作$V'$，这个$V'$的size是k，而且是CLIQUE。
因为$V'$中任意两个，都是不同组的，而且他们并不互补（否则他们不可能都是1），所以根据我们的构造，他们是相连的。

* `<=`: 如果构造出来的G确实有size为k的CLIQUE，证明$\phi$可以satisfy:
该clique中的k个点两两相连，那么所有这k个点都不可能在同一组中（因为同一组的不相连）。
因为总共有k组，那么刚好每一组有一个。
我们可以将这些点都assign为1,因为他们不包含互斥的。这种assign可以让$\phi$满足。


VERTEX-COVER
-------------------

* `英文定义`：
A **vertex cover** of an undirected graph $G=(V,E)$ is a subset $V' \subseteq V$
such that if $(u,v) \in E$ then $u \in V'$ or $v \in V'$ or both.
* `中文定义`:vertex cover是无向图G的顶点的一个子集$V'$，使得G中任意一条边，至少有一个顶点在其中。
* `vertex cover problem`: 找到这么一个满足条件的$V'$，其size最小。
* `decision problem`: 决定G是否有一个size为k的vertex cover
* `正式定义`:
VERTEX-COVER={$<G,k>$: G has a vertex cover of size k}

### 证明NPC

* `NP`:
对于certificate $V'$，我们检测1.size is k 2. G中所有edge，检测是否有点在其中。

* `reduction`: CLIQUE $\le_P$ VERTEX-COVER

* `构造`:
一个CLIQUE的instance $G(V,E)$. $G'(V,\overline{E})$.
也就是，$G'$包含所有顶点，但是边恰好相反。
对应问题是$G'$有$|V|-k$size的vertex cover


* `=>`:
G有CLIQUE of size k. 在$G'$中，我要证明任何一条边，都有顶点在$V-V'$中。
对$G'$中的任何一条边，有：它不在G中。
那么，至少有一个顶点不在$V'$中（$V'$中顶点都是两两相连的）。
所以至少有一个顶点在$V-V'$中。

* `<=`:
$G'$有vertex cover $V'$ of size k. 在G中，要证明$V-V'$中的顶点两两相连。
有两个点，他们都不在$V'$中（也就是他们都在$V-V'$中)，
那么他们在$G'$中就肯定不相连（如果相连，必然有至少一个在$V'$中）。
那么他们在G中肯定相连。


Hamiltonian-cycle
-------------------

* `英文定义`: a hamiltonian cycle of an undirected graph
is a simple cycle that contains each vertex in V.
* `中文定义`: 无向图中的一条可以包含所有顶点有且仅有一次的圈。
* `problem`: G是否有这么一条路径。
* `正式定义`: HAM-CYCLE={$<G>$: G is a hamiltonian graph(G has a ham cycle)}

### 证明NPC

* `NP`: certificate是一条路径，直接验证这条路径是否包括所有顶点有且只有1次，并且开始点就是结束点。
* `reduction`: VERTEX COVER

* `构造`

现在我们有图$G=(V,E)$，有size为k的vertex cover. 对每一条边，我们设置一个Widget.如下图
![image](https://farm9.staticflickr.com/8568/15887792145_c83e588b4c_m.jpg)

只能从四个角进出。这样的话，为了遍历所有点，那么进出的方式只能是下面两种。

![image](https://farm9.staticflickr.com/8609/15700237978_576f557c45_n.jpg)

**第一种边** 就是widget中包含的边，每个14条。

**第二种边**

对于每一个widget，$W_{uv}$，我们找到所有u相连的边，并把他们随意排序。
将第i个（$W_{ui}$）的左下角的和第i+1个的左上角连起来。
如果是$W_{vu}$，一样，变成右上角和右下角。
也就是，将$[u,ui,6],[u,u(i+1),1]$连起来。

用下面的图作为示范（图中应为yx,yw）

![image](https://farm8.staticflickr.com/7473/15700565650_af08a88700_m.jpg)

添加的边为

![image](https://farm8.staticflickr.com/7510/15701847019_4f4e8bffe0_n.jpg)

**第三种边**

现在再添加k个点，这些点每个都和这种点连起来：
在上一步已经排序好的路径中，第一个点的1和最后一个点的6.

![image](https://farm8.staticflickr.com/7583/15265699974_503cb70323_n.jpg)

* `=>`:

已知G有k的vertex cover，怎么证明$G'$有ham cycle.

因为有k个s，所以每个可以对应一个vertex cover。
从第一个s出发，到第一个vertex cover的点，然后沿着路径一路走下来，最后到第二个s。
然后再到第二个vertex cover，以此类推。

每次走一个widget时可以有两条路，一个是走完，一个是走全部。
如果对面的节点不是vertex cover点的话，走完。
如果对面也是，那么走一半，剩下一半给他走。

既然vertex cover可以cover所有的边，那么我们也走完了所有的点。

* `<=`:

已知$G'$有ham cycle，怎么证明G有k的vertex cover.

我们证明在这个cycle中，任何一个从s出来的直接相连的点，这k个构成vertex cover。

因为每一个widget只有两种走法，且如果s从u进入，那么后面所有的widget都是$W_{ux}$或者$W_{xu}$。
走完回到一个s。
总共只有k个路径，因为就k个s。
每个widget都会被走过，所以一定是和那条路径的u相邻。
所以这k个u就cover了所有路径。

Traveling salesman problem
----------------------------

* `英文定义`: Salesman wants to make a ham cycle among cities.
for city i and j, the cost of i to j is c(i,j) nonnegative.
He wants to make the cost minimum.
* `中文定义`：城市是两两相连的。每条边加权，做一个ham cycle，使总cost最小。
* `decision problem`:
$<G,c,k>: G is graph, c is cost function,
G has a traveling salesman tour with cost at most k.

### 证明NPC

* `NP`
* `Deduction`: Hamiltonian Cycle
* `构造`
对于一个ham cycle问题$G=(V,E)$,使用同样的图当作TSP，只不过将其所有边都连上.
构造c：c(i,j)= 0 if $(i,j) \in E$ and 1 otherwise.
k=0.

* `=>`:
如果ham cycle有解，那么这条路全是0,则TSP显然有解。

* `<=`:
如果TSP有0解，那么这条0解上的所有路都是0.
那么所有的边都在G中。那么该路径也是G的ham cycle。

Subset sum problem
----------------------

* `英文定义`: we are given a finite set S of positive integers and an integer target t>0.
We ask whether there exists a subset $S' \subseteq S$ whose sum is t.
* `中文定义`：给定一个整数集S和一个目标t，S中是否存在一个子集其sum为t。
* `正式定义`：
SUBSET-SUM={$<S,t>$: there exists a subset $S' \subseteq S$ such that $t=\sum_{s\in S'} s}$.

### 证明NPC

* `NP`
* `reduction`: 3-CNF-SAT
* `构造`
假设总共有n个$x_i$，总共有k个clause：$C_i$.

有这么两个假设。没有任何clause包含一对相反的变量，如$x$ and $\neg x$.
因为这么一个clause一定是1,所以无所谓。
第二个假设是每个变量都至少出现在一个clause里。
因为如果这个变量没有出现在任何clause里，那么他是什么也无所谓了。

对每一个x，搞2个值v。每个C搞两个值s.
下图中是用10进制表示，最右边是最低位。
只有右上角一块是变的，原则是：如果C中有$x_i$，那么$v_i$相应位置1.否则置0.$v'$刚好相反。

![image](https://farm8.staticflickr.com/7541/15886319881_0bc44428a3_n.jpg)


* `=>`
已知3-CNF-SAT有解，证明Subset sum有解。

我们有一个assignment for x that make 3-CNF-SAT satisfies.
对于这个assignment，如果$x_i=1$, 那么将$v_i$包含进去，不包含$v'_i$。
这样，前几位都是1,满足t。
后面几位，对每一位，不可能全是0,那样的话这个Clause就是0了。
所以后面几位相加是1-3.
然后从s中选出能匹配为4的。

* `<=`
已知subset sum有解，证明3-CNF-SAT有解。

subset sum的那个子集中，包含的v肯定是不会同时有$v_i$和$v'_i$。
如果有$v_i$，那么assignment $x_i$为1,否则为0.
我们证明这个assignment能使3-CNF-SAT满足。

如果$C_i$对应的v都是0,那么那一位就不能构成4了，这不可能，所以C至少有一个对应的v是1.
这个v也保证了该C是为1的。
所有C都是1了，所以就satisfies了。
