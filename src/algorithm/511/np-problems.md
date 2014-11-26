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

CLIQUE = { <G,k>: G is a graph containing a clique of size k}
