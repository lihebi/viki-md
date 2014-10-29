# R-Trees

* `title`: R-Tree: A Dynamic Index Structure For Spatial Searching
* `Author`: Antonin Guttman, UCB
* `date`: 1984 ACM
* `CiteBy`: 7218 util 10/29/2014
* `link`: http://www-db.deis.unibo.it/courses/SI-LS/papers/Gut84.pdf

## Problem

No Indexing method suited to **data objects of non-zero size located in multi-dimensional spaces**.

## Contributions

* Describe a dynamic index structure called R-Tree to meet the problem.
* Give algorithms for searching and updating it.
* Implementation and Performance.

## Comments

In CondenseTree algorithm, when a node has fewer than `m` entries,
delete the node and add **ALL Entries of N** to `Q`.
Then In the end, reinsert all in Q, which must be costy.
