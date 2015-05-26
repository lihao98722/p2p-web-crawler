__author__ = 'Howie'


from p2p_web_crawler.peer import DOMAIN_SEEN, DOMAIN_PEER_IP_MAP
import p2p_web_crawler.url_processor as url_processor
from p2p_connector.common import dispatch_url


class Dispatcher:
    def __init__(self, links):
        self.links = links

    # dispatch links to their corresponding peers
    def dispatch(self):
        print("dispatch here!")
        for link in self.links:
            domain = url_processor.get_domain(link)
            dest_ip = DOMAIN_PEER_IP_MAP.get(domain)
            self.send_to_other_peers(link, dest_ip)

    def send_to_other_peers(self, link, dest_ip):
        # for test only
        dest_ip = "192.168.199.164"
        # twisted can not transfer unicode data, so encode string with "utf-8" EXPLICITLY
        link = link.encode("utf-8")
        dispatch_url(dest_ip, [link, ])