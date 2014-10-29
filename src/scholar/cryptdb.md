# CryptDB

CryptDB: Protecting Confidentiality with Encrypted Query Processing

* `Author`: Raluca Ada Popa
* `date`: 2011
* `site`: 205 util 10/29/2014
* `link`: http://www.mit.edu/~ralucap/CryptDB-sosp11.pdf

## Problem

Online apps are vulnerable because:

* adversaries can exploit software bugs to gain access to private data
* curious or malicious administrators capture and leak data

## Idea

Provide practical and provable confidentiality for the problem.

* execute SQL queries over encrypted data using a collection of efficient SQL-aware encryption schemes.
* chain encryption keys to user passwords

## Result

* A database administrator never gets access to decrypted data
* even if all servers are compromised, an adversary cannot decrypt data of user who is not logged in
