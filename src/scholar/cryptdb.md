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

## Chanllenges

* `最小化给数据库的密钥。最大化query语句执行效率。`tension between **minimizing confidential info revealed to the DBMS** and **efficiently execute queries**
* `应用服务器被攻破后也能保护。`minimize data leak when application server is compromised, in addition to DBMS server

## Idea

Provide practical and provable confidentiality for the problem.
`实际且证明有效的算法。`

* `在加密过的数据上执行SQL语句。`execute SQL queries over encrypted data using a collection of efficient SQL-aware encryption schemes.
* adjustable query-based encryption
* `用每个用户的key来加密。`chain encryption keys to user passwords

## Result

* `数据库管理员无法单从数据库上获取明文信息。`A database administrator never gets access to decrypted data
* `应用服务器也被攻破了？没有登的信息还是可以得到保护。`even if all servers are compromised, an adversary cannot decrypt data of user who is not logged in
