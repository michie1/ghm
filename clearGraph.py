import xmlrpclib
server = xmlrpclib.Server('http://localhost:20738/RPC2')
G = server.ubigraph
G.clear()
