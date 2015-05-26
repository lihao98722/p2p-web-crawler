#-*-coding:utf-8-*-
__author__ = 'Howie'

import json
import p2p_web_crawler.peer as peer


MY_IP = "192.168.199.207"
PORT = 10001
NODE_TABLE = ['192.168.199.164', '192.168.199.207']
CLIENTS = {}
MSG_NOTATION = "#msg_end"


def dispatch_url(peer_ip, url_list):
    target_protocol = CLIENTS[peer_ip]
    url_list_json = {"urls": url_list}
    target_protocol.transport.write(json.dumps(url_list_json) + MSG_NOTATION)


def notify_domains_update():
    domain_list = list(peer.DOMAIN_SEEN)
    domain_list_json = {"domains": domain_list}
    for peer_ip in NODE_TABLE:
        if peer_ip != MY_IP:
            target_protocol = CLIENTS[peer_ip]
            target_protocol.transport.write(json.dumps(domain_list_json) + MSG_NOTATION)