# P & NP & NPC


## Homeworks

### 34.1-6

把P作为语言，证明其对`并，交，连，补,*`是封闭的。

If $L_1,L_2 \in P$, then

* $L_1 \bigcup L_2 \in P$
* $L_1 \bigcap L_2 \in P$
* $L_1 L_2 \in P$
* $\overline{L_1} \in P$
* $L_1^* \in P$

**Solution**

Assume $L,L_1,L_2 \in P$:

* decide if $x \in L_1$ and $x \in L_2$. 只要有一个成立，就会有$x \in L_1 \bigcup L_2$. Otherwise not.
* 同上，只要两个都成立，就有$x \in L_1 \bigcup L_2$. Otherwise not.
* $L_1,L_2$是两个字符串，$L_1L_2$是把两个连接起来。用$x_ij$来表示一个字符串的子串。
对于所有n种k，decide$x_1k \in L_1$, $x_(k+1)n \in L_2$.
* $x \in \overline{L}$ 等价于 $x  L$
