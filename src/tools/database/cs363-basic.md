# Database

## concepts

* `attribute`: column name
* `relation scheme`: a set of attributes
* `tuple`: S is a scheme. A tuple over S is an assignment of values to attributes of S.
* `superkey`: a set of attributes that identify tuples uniquely
* `key`: a minimal set of attributes that form a superkey
    * a key can have multiple attributes, for example, `{CourseCode, StudentID}`.
    * a relation can have multiple keys. `r(A,B,C,D,E)` can have `{A,B,C}` and `{B,D}` as its key
* `primary key`: impose an ordering of tuples in a relation. Only one primary key.
* `foreign key`: a foreign key should be a primary key in some other relations.

## operations

* `selection operator`: select tuples of r that satisfy condition c

$\rho_c(r)$

* `projection operator`: retains only X columns. X can be AC, to choose column A and C from r to form a new table.

$\prod_X(r) = {x[X]:x \in r}$

| A | B | C |
| :---: | :---: | :---: |
| 1 | 2 | 4 |
| 5 | 4 | 2 |
| 5 | 6 | 2 |
| 7 | 8 | 3 |

$\prod_{AC}(r)$

| A | C |
| :---: | :---: |
| 1 | 4 |
| 5 | 2 |
| 7 | 3 |
