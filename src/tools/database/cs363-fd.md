Functional Dependency
=====================

chapter 10: data dependencies and database schema design

Problem to be solved
--------------------

Given Attributes(column names) and Constraints, design a database schema.

### Supplier Parts Example

* A: {Supplier, Address, Item, Price}
* C:
  * C1: Supplier的Address唯一
  * C2: 同一个supplier对一件item的定价唯一

| S | A | I | P |
| :--- | :--- | :--- | :--- |
| A | Ames | Nut | 0.5 |
| A | Ames | Bolt | 0.6 |
| B | DSM | Nut | 1.0 |

这种设计的问题：Addr重复多次

* 每次添加一条记录，都需要addr
* 每次更新addr全部记录都要更新
* 删除了最后一条A的记录，相应的addr就没了

改进的设计: {SA} and {SIP}

functional dependencies
---------------------

### 几个定义

* `C-legal`: a database state is C-legal if it satisfies all C localized update.
That is, no changes or inputs are required from other relations.
* `functional dependencies`: `S->A`, reads "S determines A", is a functional dependencies.
Given a S value, there is a unique A value.

### 性质(Armstrong's rules)

* transitivity: X->Y, Y->Z => X->Z
* reflexivity: ABC->BC
* augmentation: X->Y => XW->YW

### losslessness

a decomposition (R1,R2) is lossless if and only if
$R_1 \vedge R_2$至少能决定R1,R2中的一个。

### redundancy (BCNF)

* r: 一个relation
* R: ABCDEF, 即所有的attr集合

r is a relation over R. Then we say that R is in BCNF if:
如果X->A在R中成立，那么要不然X->A是trival的，要不然X是R的superkey.

trival: AB->A, A->A

如果X->A是BCNF的冲突，那么如下分解的两个都是BCNF的：(XA,R-A)

### F+

suppose F is a set of fds, then F+ denotes the set of all fds that can be deduced from F.

If F holds in a db, then F+ is the set of all fds hold in it.

If F holds, F+ holds, G+=F+, then we have G holds.
