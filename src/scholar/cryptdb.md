# CryptDB

* `title`: CryptDB: Protecting Confidentiality with Encrypted Query Processing
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



## 全文翻译

### 1. Introduction
private信息不安全。漏洞可以获取server权限;应用服务器管理员会做坏事;物理上接触server的人可以直接从硬盘和内存中读。

naive方法：

* 极端：所有数据加密，在客户端解密，在客户端运算。有些运算需要做运算在大量数据上;将现有server应用转换到client上比较困难。`TODO server上不做运算，或者做少量数据量大的运算。怎样easy的将数据转换到client上来做？`
* 完全同态加密。server运行所有函数，都可以对加密的数据使用，client看到解密数据。太慢不实际。

CryptDB处理情形：数据库和分离的应用服务器。两种thread：

* DBA从数据库上泄漏数据
* Hacker得到数据库和应用服务器的权限。

两个chanllenge：

* 最小化给数据库的密钥。最大化query语句执行效率。现有方法不是太慢就是安全不够，或者功能不强（有些query执行不了）
* 应用服务器被攻破后也能保护。

cryptDB解决这些的3个key idea

* 在加密数据上执行query。
实现这个想法，通过 *SQL-aware encryption strategy*，
利用的是所有SQL语句都是由well-defined原语组成的，
比如equality check,order comparison,sum,join.
使用现有的encryption scheme（对equality,sum,order),
和新的privacy-preserving cryptographic(对join)。
为什么快？mostly使用对称加密，避免同态加密，而且不用修改数据库结构。
* adjustable query-based encryption. 自适应改变加密策略。
想要执行特定的功能的语句（order,euqlity)，需要泄漏更多信息。
但是也有不泄漏的加密，但是不能执行一些语句。
所以对不同数据使用不同加密。
但是我们只有在运行的时候才能知道操作到底需要什么功能。
使用`onions of encryption`。
紧密的存储多个密文。
* chain encryption keys to user passwords.
数据只能通过对应用户的密码来解。
结果是就算应用服务器被攻破了没，不登录的用户是安全的。
为了构造这个chain，developer在应用的SQL schema上提供policy annotations。

### 2. Security Overview
#### Thread1: 数据库
#### THread2: 应用server也被攻破

### 3. Queries over encrypted data
#### SQL-aware encryption
encryption type. 对于每一个type，讨论cryptdb需要的安全属性，功能，实现。

* Random(RND)
* Deterministic(DET)
* Order-preserving encryption(OPE)
* Homomorphic encryption(HOM)
* Join(JOIN and OPE-JOIN) 新的。
* Word search(SEARCH)

#### Adjustable Query-based Encryption
#### Executing over Encrypted Data
#### Computing Joins
#### Improving Security and Performance

### 4. Multiple Principals
### 5. Application case studies
### 6. discussion
### 7. implementation
### 8. experimental evaluation
### 9. related work
### 10. conclusion
