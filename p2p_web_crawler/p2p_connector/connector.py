#-*-coding:utf-8-*-
__author__ = 'fellow'


import socket
from twisted.internet import reactor
from common import PORT, NODE_TABLE, CLIENTS
from twisted_server import RecvFactory
from twisted_client import SendFactory


class Connector():

    def __init__(self):
        pass

    @staticmethod
    def start():
        local_ip = socket.gethostbyname(socket.gethostname())
        print "local ip : " + local_ip
        print "initialize connector..."
        # server get ready
        receive_factory = RecvFactory()
        reactor.listenTCP(PORT, receive_factory)
        # client get ready
        send_factory = SendFactory()
        for node_ip in NODE_TABLE:
            if node_ip != local_ip:
                reactor.connectTCP(node_ip, PORT, send_factory)

