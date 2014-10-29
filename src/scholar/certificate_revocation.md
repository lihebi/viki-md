# Certificate Revocation

* `title`: certificate revocation and certificate update
* `author`: Moni Naor
* `cite`: 506 until 10/30/2014
* `publish`: 2000
* `link`: https://www.usenix.org/legacy/publications/library/proceedings/sec98/full_papers/nissim/nissim.pdf

## Problem

Wide use of public key cryptography 需要验证 authenticity of public keys.
使用的是Public Key Infrastructure(PKI)的certificate, 包括key和过期时间。
过期时间之前，想要把它revoke掉。怎么做？

## Contribution

* new solution for problem of certificate revocation
* solution gains in `scalability`, `communication costs`, `robustness to parameter changes and update rate`

## Idea

Create and maintain efficient `authenticated data structures` holding info about validity of certificates.

在他们设计的data structure中，怎么找到`authenticate directory`。
也就是，核心是`authentiated search data structures`.

## concepts

* `a certificate`: message signed by a 
publicly trusted authority(也叫`certification authority`,`CA`,其public key通过其他途径已经获得。)
,which include a public key and expireation date.
负责给别人分发public key.
* `Directory`: 不可信的组织，提供来自CA的`updated certificate revocation info`，供用户查看
