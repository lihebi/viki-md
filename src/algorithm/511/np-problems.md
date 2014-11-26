NP Problems
==============

CLIQUE
--------------

英文定义：

A clique in an undirected graph $G=(V,E)$ is a subset $V' \subseteq V$ of vertices,
each pair of which is connected by an edge in E.

首先，clique是无向图G中的一个子集。这个子集中的所有点在G中是两两相连的。
也就是说，clique is a complete subgraph of G.

我们定义`size of clique`为该子集中的顶点个数。
那么`clique problem`就是要找到最大的CLIQUE.

将该最优化问题转换成decision problem,得：对于一个图G，是否存在size为k的clique.

正式定义CLIQUE问题：

CLIQUE = { $<G,k>$: G is a graph containing a clique of size k}

### 证明CLIQUE是NP-complete

首先证明NP: 对于一个图$G=(V,E)$，我们用$V' \subseteq V$来表示一个certificate。
为了验证$V'$是否是clique，我们检查每一个pair $u,v \in V'$，其边$(u,v) \in E$.
可以在Polynomial Time内实现。

然后证明NP-Hard. 证明$3-CNF-SAT \le_P CLIQUE$.

构造：对于任何一个3-CNF-SAT，设其有k个clause,每个clause有3个变量。也就是：
$\phi = (x_1 \vee x_2 \vee \neg x_3) \wedge \ldots$
把所有的变量（允许重复）都放入G中。
对与每组中三个变量的每一个，将其与其余所有组的所有变量连接，除非他们互补（$x$ and $\neg x$）。

如果$\phi$有一个satisfying assignment，那么：
其中的每一组至少有一个变量是1.把这些变量全部取出来当作$V'$，这个$V'$的size是k，而且是CLIQUE。
因为$V'$中任意两个，都是不同组的，而且他们并不互补（否则他们不可能都是1），所以根据我们的构造，他们是相连的。

如果构造出来的G确实有size为k的CLIQUE，证明$\phi$可以satisfy:
该clique中的k个点两两相连，那么所有这k个点都不可能在同一组中（因为同一组的不相连）。
因为总共有k组，那么刚好每一组有一个。
我们可以将这些点都assign为1,因为他们不包含互斥的。这种assign可以让$\phi$满足。
