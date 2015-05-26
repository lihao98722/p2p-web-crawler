__author__ = 'fellow'

from twisted.internet import protocol
from common import PORT, NODE_TABLE, CLIENTS


class ReceiverProtocol(protocol.Protocol):
    connect_number = 0

    def __init__(self):
        pass

    def connectionMade(self):
        ip = self.transport.getPeer().host
        print "Client (%s) get connected" % ip
        # update CLIENTS dict
        CLIENTS[str(ip)] = self
        # update num of connection
        ReceiverProtocol.connect_number += 1
        # connection COMPLETE
        if ReceiverProtocol.connect_number == len(NODE_TABLE)-1:
            print "connection complete!"

    def connectionLost(self, reason):
        ip = self.transport.getPeer().host
        print "Client (%s) lost the connection" % ip
        # delete the lost connection
        del CLIENTS[str(ip)]
        # update num of connection
        ReceiverProtocol.connect_number -= 1

    def dataReceived(self, data):
        print 'Message from client(%s):%s' % (self.transport.getPeer(), data)


class RecvFactory(protocol.ServerFactory):
    protocol = ReceiverProtocol

    def __init__(self):
        pass
