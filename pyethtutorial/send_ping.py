from discovery import EndPoint, PingNode, PingServer
import os

IP_ADDRESS = os.environ.get("IP_ADDRESS", "")

my_endpoint = EndPoint(unicode(IP_ADDRESS), 30303, 30303)
their_endpoint = EndPoint(u'127.0.0.1', 30303, 30303)

server = PingServer(my_endpoint)

listen_thread = server.udp_listen()
listen_thread.start()

server.ping(their_endpoint)