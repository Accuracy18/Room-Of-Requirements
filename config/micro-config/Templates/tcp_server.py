from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ${service_type}Factory

from twisted.application.service import Application
from twisted.application.internet import TCPServer, SSLServer, ClientService, backoffPolicy

from twisted.internet.defer import inlineCallbacks, Deferred, DeferredList
from twisted.internet.task import LoopingCall

from twisted.internet.endpoints import clientFromString

% if protocol == 'mqtt':
from mqtt.client.factory import MQTTFactory
% endif

% if is_ssl:
from twisted.internet.ssl import DefaultOpenSSLContextFactory, ClientContextFactory
% endif

<%def name="credentials()">
<h1>Hello, ${name}!</h1>
from twisted.cred.checkers import ICredentialsChecker
from twisted.cred.credentials import IUsernamePassword, UsernamePassword
from twisted.cred.portal import Portal, IRealm
</%def>

<%def name="web()">
from klein import Klein
from twisted.web.server import Site, Session, NOT_DONE_YET
from twisted.web.resource import Resource
</%def>

<%def name="sql_plugin()">
from twisted.enterprise.adbapi import ConnectionPool
from twisted.python.components import registerAdapter
from zope.interface import implementer, Interface, Attribute

sql_pool = ConnectionPool('mysql.connector', host=, user=, passwd=, db=)
</%def>

from twisted.internet.stdio import StandardIO
import json

<%def name="regular_tcp()">
class ${protocolName}(Protocol):
        
    def connectionMade(self):
        pass
    
    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        pass
</%def>

<%def name="mqtt_service()">
class IotShit(ClientService):

    def __init(self, endpoint, factory):
        ClientService.__init__(self, endpoint, factory, retryPolicy=backoffPolicy())

    def startService(self):
        self.whenConnected().addCallback(self.connectToBroker)
        ClientService.startService(self)

    def connectToBroker(self, protocol):
        protocol.setWindowSize(3)
        protocol.onPublish = self.onPublish

        match protocol.factory.profile:
            case 1:
                protocol.connect("TwistedMQTT-pub", keepalive=60).addCallback(self.subscribe, protocol)

            case 2:
                LoopingCall(self.publish, protocol).start(2)
                protocol.connect("TwistedMQTT-pub", keepalive=60).addCallback(lambda x: print(x))

    def publish(self, protocol):

        d1 = protocol.publish(topic="something/fat", qos=1, message="jojo on frankie").addErrback(lambda x: x)

        d2 = protocol.publish(topic="something/cat", qos=0, message="hello world 1").addErrback(lambda x: x)

        d3 = protocol.publish(topic="something/bat", qos=2, message="hello world 2").addErrback(lambda x: x)

        dlist = DeferredList([d1,d2,d3], consumeErrors=True)
        dlist.addCallback(lambda x: print(x))
        return dlist

    def subscribe(self, result, protocol):

        d1 = protocol.subscribe("fat/something", 0).addCallbacks(lambda x: print(x), lambda x: print(x))

        d2 = protocol.subscribe("cat/something", 0).addCallbacks(lambda x: print(x), lambda x: print(x))

        d3 = protocol.subscribe("bat/something", 0).addCallbacks(lambda x: print(x), lambda x: print(x))

        dlist = DeferredList([d1,d2,d3], consumeErrors=True)
        dlist.addCallback(lambda x: print(x))
        return dlist


    def onPublish(self, topic, payload, qos, dup, retain, msgId):
        print(payload)
        
factory = MQTTFactory(profile=MQTTFactory.PUBLISHER)
#factory = MQTTFactory(profile=MQTTFactory.SUBSCRIBER)
</%def>


${regular_tcp()}

factory = ${service_type}Factory()
factory.protocol = ${protocolName}

% if is_ssl:
service = SSLServer(${port}, factory, DefaultOpenSSLContextFactory('path to key', 'path to crt'))

% elif is_mqtt:
endpoint_x = clientFromString(reactor, "tcp:test.mosquitto.org:1883")
service = IotShit(endpoint_x, factory)

% else:
service = TCPServer(${port}, factory)

% endif
