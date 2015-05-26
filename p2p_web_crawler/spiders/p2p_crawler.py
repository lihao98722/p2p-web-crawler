__author__ = 'Howie'

from threading import Thread
import time
import scrapy
from scrapy.conf import settings
import p2p_web_crawler.utils as utils
import p2p_web_crawler.url_processor as url_processor
from p2p_web_crawler.peer import DOMAIN_SEEN, DOMAIN_PEER_IP_MAP, URLS_TO_BE_CRAWLED
from p2p_web_crawler.items import P2PWebCrawlerItem
from p2p_web_crawler.dispatcher import Dispatcher
from p2p_web_crawler.p2p_connector.connector import Connector
from p2p_web_crawler.p2p_connector.common import notify_domains_update


class P2pCrawler(scrapy.Spider):
    name = "p2p_spider"


    def __init__(self, category=None, *args, **kwargs):
        super(P2pCrawler, self).__init__(*args, **kwargs)
        # self.start_urls = settings['INIT_URLS']
        self.start_urls = ["http://howieli.me"]
        self.init_peer_status()
        # Connector.start()
        # time.sleep(15)

    def init_peer_status(self):
        for url in self.start_urls:
            DOMAIN_SEEN.add(url_processor.get_domain(url))

    def parse(self, response):
        # yield Item to pipeline
        item = P2PWebCrawlerItem.get_item(response)
        yield item
        links = utils.extract_links(response)
        # print("analyze here!")
        # generate new request from extracted links
        for link in links:
            domain = url_processor.get_domain(link)
            if domain in DOMAIN_SEEN or domain not in DOMAIN_PEER_IP_MAP.keys():
                yield scrapy.Request(url=link, callback=self.parse)
                links.remove(link)
                # if domain is new, crawl by self, and then notify other peers
                if domain not in DOMAIN_SEEN:
                    DOMAIN_SEEN.add(domain)
                    # notify_domains_update()

        # generate new request from urls sent by other peers
        while len(URLS_TO_BE_CRAWLED) > 0:
            url = URLS_TO_BE_CRAWLED.popleft()
            yield scrapy.Request(url=url, callback=self.parse)

        # new thread dispatching links that should be crawled by other peers
        # dispatcher = Dispatcher(links)
        # dis_thread = Thread(target=dispatcher.dispatch)
        # dis_thread.start()