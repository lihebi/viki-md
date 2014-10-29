# Authentic Data Publication

* `title`: Authentic Data Publication over the Internet
* `author`: Premkumar Devanbu, UCD
* `publish`: 2003
* `cite`: 120 until 10/20/2014
* `link`: http://sirius.cs.ucdavis.edu/publications/jcs1.pdf

## problem

For large data that changes infrequently but is queried at high rate,
how to republish it securely through insecure network.

## idea

* seperate roles of data owner and data publisher
* a few digital signatures on the part of the owner
* no trust required of a publisher

## contribution

* first work to give general approaches for reducing the trust required of publishers of large databases.

## general concepts in the paper

* `Hash function`:
map digital data of arbitrary size to digital data of fixed size
* `cryptographic hash function`:
a hash function that is considered practically impossible to invert.
`ONE WAY hash function`
* `hash tree` `merkle tree`:
non-leaf node is labeled with the hash of labels of its children nodes.
FOR: efficient and secure verification of large data structure.
