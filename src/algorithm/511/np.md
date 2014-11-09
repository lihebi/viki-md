P & NP & NPC
=============================

P & NP & NPC
-----------------------------

* `class P`: consists of problems that are solvable is polynomial time.
* `class NP`: consists of problems that are verifiable in polynomial time.
* `varifiable`: given a certificate of a solution,
we could **verify that the certificate is correct**
in time polynomial in the size of the input to the problem.

$P \subseteq NP$

* `NPC`: NP-complete. it is in NP and is as hard as any problem in NP.

If any `NP-complete` problem can be solved in polynomial time,
every problemm in `NP` has a polynomial algorithm.

* `co-NP`: the set of languages L such that $\overline{L} \in NP$

### 3 key concepts in showing a problem to be NP-complete

#### Decision problem and optimization problem

`Optimization problem`:
each feasible solution has an associated value,
we wish to find one with the best value.

`Decision problem`: Answer is *yes* or *no*

Optimization problem 可以加一个 threshold 让它变成 decision problem.
因此，只要OP是简单的，DP也是简单的。

#### Reductions

已经知道problem B是P，
如果有一个procedure that transform
**any** instance $\alpha$ of A into
**some** instance $\beta$ of B
with the following characteristics:

* the transformation takes polynomial time
* the answers are the same.
That is, the answer for $\alpha$ is *yes* if and only if answer for $\beta$ is *yes*

the procedure is called `a polynomial-time reduction algorithm`.

显而易见，解决A的方法是：

1. given an instance $\alpha$ of A, use procedure to transform it into $\beta$ of B.
2. run P on B
3. use answer of $\beta$ for $\alpha$.

对于NPC，我们使用其inverse:
Assume No P algorithm for A. Assume A is NPC, we can prove B is also NPC.

#### A first NPC problem

Intro problems
-----------------------------

* `an instance of a problem`: the input to a problem. E.g. Graph G for PATH problem.

### Shortest simple path

一个有向图中，找到从一个起点出发的最短路径。

**complexity**: 即使包含负边，也可以在$O(VE)$找到。

### Longest simple path

仅仅决定一个图中是否含有一条path，包括一个给定数字以上的路径.

**complexity**: 都是`NP-Complete`。

### Euler tour

在一个连同有向图中，一个cycle，遍历所有边有且仅有一次。

**complexity**: 决定一个图是否含有Euler tour，$O(E)$.

### hamiltonian cycle

在一个有向图中，a simple cycle，包括所有顶点。

**complexity**: 决定一个有向图是否含有hamiltonian cycle是`NP-Complete`

### 2-CNF/3-CNF satisfiability

* `k-CNF`: k-Conjuntive normal form
* `A boolean formula is satisfiable` if 它包括的变量去一种0和1的组合，可以使其值为1.
* `A boolean formula is in k-CNF` if it is AND of clauses of **ORs of exactly k variables or their negations**.

$(x_1 \vee \neg x_2) \wedge (\neg x_2 \vee x_3) \wedge (\neg x_2 \vee \neg x_3)$ is 2-CNF.

**complexity**:
determine whether 2-CNF is satisfiable is P,
determine whether 3-CNF is satisfiable is NP-complete

NPC and reducitility
-----------------------------

### reducitility

* language $L_1$ is **polynomial-time reducible** to $L_2$, written $L_1 \le_p L_2$,
if 存在P时间的函数f, s.t. $x \in L_1$ if and only if $f(x) \in L_2$

意味着问题$L_1$可以转化成问题$L_2$，所以只要$L_2$有解，$L_1$同样有解。
$L_1$ is not more than a polynomial factor harder than $L_2$.

`Lemma 34.3`: if $L_1 \le_p L_2$, then $L_2 \in P$ implies $L_1 \in P$.

### NPC & NPH

a language $L \subseteq {0,1}^*$ is `NP-complete` if:

1. $L \in NP$
2. $L' \le_p L$ for every $L' \in NP$

`NP-hard`: L satisfies 2 but not 1.

`Theorem 34.4`: 如果任意一个NPC problem都是P solvable的，那么$P=NP$.
如果任意NP problem都不是P solvable的，那么所有NPC problem都不是P solvable的。

NPC Problems
-----------------------------

### clique

图中选出一些顶点，两两相连。

Homeworks
-----------------------------

### 34.1-6

把P作为语言，证明其对`并，交，连，补,*`是封闭的。

If $L_1,L_2 \in P$, then

* $L_1 \bigcup L_2 \in P$
* $L_1 \bigcap L_2 \in P$
* $L_1 L_2 \in P$
* $\overline{L_1} \in P$
* $L_1^* \in P$

#### Solution

Assume $L,L_1,L_2 \in P$:

* $L_1 \bigcup L_2$: decide if $x \in L_1$ and $x \in L_2$. 只要有一个成立，就会有$x \in L_1 \bigcup L_2$. Otherwise not.
* $L_1 \bigcap L_2$: 同上，只要两个都成立，就有$x \in L_1 \bigcap L_2$. Otherwise not.
* $L_1L_2$: $L_1,L_2$是两个字符串，$L_1L_2$是把两个连接起来。用$x_{ij}$来表示一个字符串的子串。
对于所有n种k，decide$x_{1k} \in L_1$, $x_{(k+1)n} \in L_2$.
* $\overline{L}$: $x \in \overline{L}$ 等价于 $x \notin L$
* $L^*$:

`Kleene star`: $L^*=\bigcup_{i\in N}L^k$ where $L^(k+1) = LL^k$.

我们证明对于所有k,有$\bigcup_{i=0-k}$成立。用induction.

当$k=0$，空集，显然。

假设k成立，对于k+1，有$L^{k+1}=LL^k$。

### 34.2-9

Prove that $P \subseteq co-NP$

#### Solution

$L \in P$ => $\overline{L} \in P \subseteq NP$

### 34-1

#### Solution

a).

INDEPENDENT-SET = { $ < G,k > $:G is a graph containing a independent-set of size k }

图中选出一些顶点，两两不连。

Prove NPC:

证明是NP. 构造一个验证。$V((G=(V,E), K), C)$，其中C是certificate,也就是一个顶点集，用来判断是不是Independent set。
需要做两件事：1. $|C| \le K$ 2. C构成independent set。 两个都可以在P内完成。

证明是NP-hard。用clique来推导。根据G，构造一个$G'$，顶点不变，所有边去掉，所有没有边的加上边。
这时候，有：
如果nodes are independent set in $G$, then they form a clique in $G'$;
如果nodes form a clique in $G'$, then they are independent set in $G$.

b).

1. find the maximum size independent set. Since $K \le |V|$, $O(V)$.
2. Once the maximum K is found, we need to 决定哪些v在里面。

在G中选一个v，将其和所有其他顶点相连。黑箱测试$(G',K)$。
如果成功，说明v不在independent set中。$G=G'$.继续测试下一个v。
如果失败，说明v在set中。用G做下一个v的测试。

复杂度分析：共有v个点，每个点要连其余v-1个点，共$O(V^2)$.

c).

每个节点的degree都是2，说明，是一个cycle。显然，every other vertex. 直接选出来就可以了，所以$O(V)$.

d).

maximum independent set is the side with the larger number of vertices.
直接比较一下多少就可以，所以$O(V)$.
