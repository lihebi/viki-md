Information Integration
=======================

三种类型的方法
-----------

* Federated Databases
  * No central database.
  * 数据库两两相连，可互查。
* warehousing: 中央的db定时将不同站点的数据抓取并处理，然后按照自己的schema存入数据库。
* Mediation: 中央虚拟数据库，并不存data，但是有schema。接受用户query，将其转换并传给各site。
返回结果处理后再返回用户。

这三个可以hybrid.

Data Cube
---------

![image](https://farm8.staticflickr.com/7490/15952502922_d6615c29d0_n.jpg)

* fact tuples: 2x3
* all tuples: 3x4
* summary tuples: 3x4-2x3
