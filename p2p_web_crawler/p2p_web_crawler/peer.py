__author__ = 'Howie'
from collections import deque


DOMAIN_SEEN = set()
DOMAIN_PEER_IP_MAP = dict()
URLS_TO_BE_CRAWLED = deque()


def update_domain_peer_ip_map(peer_ip, domains):
    for domain in domains:
        # if this domain has been crawled by other peers, then just do NOT crawl it anymore.
        # when encounter this domain, just dispatch it to the corresponding peer.
        if domain in DOMAIN_SEEN:
            DOMAIN_SEEN.remove(domain)
        DOMAIN_PEER_IP_MAP[domain] = peer_ip


# add urls dispatched by other peers to URLS_TO_BE_CRAWLED queue, and p2p_crawler will generate their Request.
def add_urls_to_crawl_queue(urls):
    for url in urls:
        URLS_TO_BE_CRAWLED.append(url)


# process messages sent from other peers
def process_data_received(peer_ip, decoded_json):
    # when it is a message containing urls to be crawled
    if "urls" in decoded_json.keys():
        urls = decoded_json.get("urls", [])
        add_urls_to_crawl_queue(urls)
    # when it is a message containing domain_peer_ip_map information
    if "domains" in decoded_json.keys():
        domains = decoded_json.get("domains", [])
        update_domain_peer_ip_map(peer_ip, domains)