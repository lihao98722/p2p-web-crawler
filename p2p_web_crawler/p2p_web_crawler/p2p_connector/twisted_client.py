# -*-coding:utf-8-*-
__author__ = 'fellow'

from twisted.internet import protocol
import time
import json
from p2p_web_crawler import peer
from p2p_web_crawler.p2p_connector.common import MSG_NOTATION


class SenderProtocol(protocol.Protocol):
    def __init__(self):
        pass

    def connectionMade(self):
        print "The connection to the server(%s) has been made." % self.transport.getPeer().host

    def dataReceived(self, data):
        print 'Message from the server(%s):%s' % (self.transport.getPeer().host, data)
        peer_ip = self.transport.getPeer().host
        # the data received is a string stream, so split it by self-defined message-notation to get message jsons.
        jsons_stream = data.split(MSG_NOTATION)
        # process each json in the stream
        for each_json in jsons_stream:
            try:
                decoded_json = json.loads(each_json)
                peer.process_data_received(peer_ip, decoded_json)
            except Exception:
                # json.loads() may crash when some json in the stream are not complete, but it is ok to lose few data.
                pass

    def connectionLost(self, reason):
        print"The connection  to the server(%s) is lost!!" % self.transport.getPeer().host


class SendFactory(protocol.ClientFactory):
        protocol = SenderProtocol

        def __init__(self):
            pass

        def clientConnectionFailed(self, connector, reason):
            print"Failed connected to the target terminal!! \n Try to reconnect to the target host 3 second later.."
            time.sleep(3)
            connector.connect()