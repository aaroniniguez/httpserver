#!/usr/bin/env python
#import os, sys
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable() ## This line enables CGI error reporting
import ssl
#from signal import signal, SIGPIPE, SIG_DFL
#from SocketServer import ThreadingMixIn
#import threading

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
#class ThreadedHTTPServer(ThreadingMixIn, server):
#    """Handle requests in a separate thread."""
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin"]
httpd = server(server_address,handler)
#srvobj = ThreadedHTTPServer(server_address, handler)
#srvobj.socket = ssl.wrap_socket (srvobj.socket, certfile="./localhost.pem", server_side=True)
# Force the use of a subprocess, rather than
# normal fork behavior since that doesn't work with ssl
#handler.have_fork=False
httpd.serve_forever()
