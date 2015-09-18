### Peer-to-peer Distributed Web Crawler
---

A high-performance distributed web crawler based on peer-to-peer architecture which ensures load-balancing and supports recovery from errors.


#### Master/Slaves vs Peer-to-peer
---

In Master/Slaves architecture, the master server is likely to crash down because of the overburdening tasks. Once the master server crashes down, the whole distributed system will break down immediately.

In Peer-to-peer architecture, each node(peer) is identical, serves both as webpages downloader and tasks dispatcher. Load-balancing and recovery machanism gurantee the stability of system.


#### Technologies
---

The system was mainly built on [Scrapy](http://scrapy.org) and [Twisted](https://twistedmatrix.com). Scrapy guarantees crawling performance of each peer, while Twisted makes sure high-performance asynchronous conferencing between them. Besides, [Redis](http://redis.io) and [MongoDB](https://www.mongodb.org) were chosen as k-v cache and database system.
