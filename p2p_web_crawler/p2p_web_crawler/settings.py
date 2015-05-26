# -*- coding: utf-8 -*-

# Scrapy settings for p2p_web_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'p2p_web_crawler'

SPIDER_MODULES = ['p2p_web_crawler.spiders']
NEWSPIDER_MODULE = 'p2p_web_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'p2p_web_crawler (+http://www.yourdomain.com)'


# PIPELINE
ITEM_PIPELINES = ['p2p_web_crawler.pipelines.MongoDBPipeline', ]


# MONGODB
MONGODB_SERVER = "192.168.199.207"
MONGODB_PORT = 27017
MONGODB_DB = "p2p"
MONGODB_COLLECTION = "web_pages"


# Crawler
INIT_URLS = ["http://www.zhibo8.cc/index.html",
             "http://howieli.me/"]
NUMBER_OF_ITEMS_TO_WRITE = 100

