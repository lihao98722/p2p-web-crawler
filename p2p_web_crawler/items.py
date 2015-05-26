# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class P2PWebCrawlerItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    peer_ip = scrapy.Field()

    @classmethod
    def get_item(cls, response):
        item = cls()
        item['url'] = response.url
        # if without title, set title to ""
        try:
            item['title'] = ''.join(response.xpath("//head/title/text()").extract()).strip()
        except Exception:
            item['title'] = ""
        item['body'] = str(response.body).decode("unicode_escape")
        item['peer_ip'] = "192.168.199.100"
        return item
