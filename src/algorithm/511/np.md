# P & NP & NPC

## P & NP & NPC

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

#### `Decision problem` and `optimization problem`

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

## Problems

* `an instance of a problem`: the input to a problem. E.g. Graph G for PATH problem.

### Shortest simple path

一个有向图中，找到从一个起点出发的最短路径。即使包含负边，也可以在$O(VE)$找到。

## Longest simple path

仅仅决定一个图中是否含有一条path，包括一个给定数字以上的路径，都时`NP-Complete`。

### Euler tour

在一个连同有向图中，一个cycle，遍历所有边有且仅有一次。

决定一个图是否含有Euler tour，$O(E)$.

### hamiltonian cycle

在一个有向图中，a simple cycle，包括所有顶点。

决定一个有向图是否含有hamiltonian cycle是`NP-Complete`

### 2-CNF/3-CNF satisfiability

* `k-CNF`: k-Conjuntive normal form
* `A boolean formula is satisfiable` if 它包括的变量去一种0和1的组合，可以使其值为1.
* `A boolean formula is in k-CNF` if it is AND of clauses of **ORs of exactly k variables or their negations**.

$(x_1 \vee \neg x_2) \wedge (\neg x_2 \vee x_3) \wedge (\neg x_2 \vee \neg x_3)$ is 2-CNF.

determine whether 2-CNF is satisfiable is P,
determine whether 3-CNF is satisfiable is NP-complete

## Homeworks

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

