# R-Trees: A Dynamic Index Structure For Spatial Searching

By: Antonin Guttman, UCB

Publish: 1984 ACM

# Problem

No Indexing method suited to **data objects of non-zero size located in multi-dimensional spaces**.

# Why Difficult?

# Contributions

* Describe a dynamic index structure called R-Tree to meet the problem.
* Give algorithms for searching and updating it.
* Implementation and Performance.

# Related Work

* B-Tree

# Basic Idea

# Argue Start!!!

In CondenseTree algorithm, when a node has fewer than `m` entries,
delete the node and add **ALL Entries of N** to `Q`.
Then In the end, reinsert all in Q, which must be costy.
