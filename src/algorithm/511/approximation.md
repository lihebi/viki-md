Approximation
=============

对于NPC问题，既然我们解决不了，我们可以另辟溪径。有3种方法：

* 当input size很小时，欠可以解出来
* 有些special case可以在P内解出来。
* 可以找一个近似解。near optimal solution

那么，什么是近似解？$C^*$

an algorithm for a problem has an approximation ratio of $\rho(n)$ if:
for input size n, 指标C表示该算法的结果，指标

$C^*$

表示最佳值，那么我们有

$max(\frac{C}{C^*}, \frac{C^*}{C}) \le \rho(n)$

比如，满足条件的最大size理论是$C^I$，而我的算法得$C=\frac{C^*}{2}$。那么$\rho(n)=2$。

Vertex-cover
------------

找到一个点的集合，能cover住所有边。要使集合最小。

```
C={}, E'=G.E
while E' != {} {
  pick an arbitrary edge (u,v) in E'
  C += {u,v} // add u and v to C
  从E'中去掉所有和u或v有关的边
}
return C
```

O(V+E)

### 证明这是2-ratio approximation solution:

1. 可以在P内完成。
2. 对于选择的每条边(u,v)，设此集合为A。
那么A中不可能有同一个点出现两次（因为我们每次都会去掉任何有关的边。）
而optimal value是一个vertex cover，那么它一定可以cover A.
所以有$|C^*| \ge |A|$.
而我们的$|C|=2|A|$。所以有$|C|=2|A| \le 2|C^*|$

Traveling-salesman problem
--------------------------

现引入一个三角限制：$c(u,w) \le c(u,v) + c(v,w)$

TSP with triangle constraint: NPC, but has 2-approximation solution
TSP without triangle constraint: NPC, and no approximation unless P=NP

```
从G中随便找个点r
以r做prim算法，找最小生成树
此树的先序遍历序列
按序列顺序相连
```

$O(V^2)$

### 证明2-approximation

$H^*$为最佳值。此$H^*$对应的hamilton cycle，减去某一条边，必然得一棵最小生成树。
设T为我们找到的树。显然有$c(T) < c(H^*)$.

定义一个full walk W为，遍历中走过的所有的边。这样每条边走过两次，去时一次，回来时一次。
有$c(W) = 2c(T)$

![image](https://farm8.staticflickr.com/7575/15998247402_0675174c32_q.jpg)

图中，full walk是: `abcbdbaea`
H是: `abcdea`
对于full walk中，去掉任何一个节点，相当于第三边直接相连了，会减少cost。
所以有$c(H)<c(W)=2c(T)<2c(H^*)$

set covering
-------------

X是点的集合，F是一组set。从F中选出一些set，可以cover住X中的所有的点。要求选出的最少。
