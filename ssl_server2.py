#!/usr/bin/env python
import os, sys
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable() ## This line enables CGI error reporting
import ssl
#from signal import signal, SIGPIPE, SIG_DFL
#from SocketServer import ThreadingMixIn
#import threading
import time

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
class getHandler(handler):
	def send_head(self):
		if self.is_cgi():
		    return self.run_cgi()
		else:
			"""Common code for GET and HEAD commands.
			This sends the response code and MIME headers.
			Return value is either a file object (which has to be copied
			to the outputfile by the caller unless the command was HEAD,
			and must be closed by the caller under all circumstances), or
			None, in which case the caller has nothing further to do.
			"""
			path = self.translate_path(self.path)
			f = None
			if os.path.isdir(path):
			    if not self.path.endswith('/'):
				# redirect browser - doing basically what apache does
				self.send_response(301)
				self.send_header("Location", self.path + "/")
				self.end_headers()
				return None
			    for index in "index.html", "index.htm":
				index = os.path.join(path, index)
				if os.path.exists(index):
				    path = index
				    break
			    else:
				return self.list_directory(path)
			ctype = self.guess_type(path)
			try:
			    # Always read in binary mode. Opening files in text mode may cause
			    # newline translations, making the actual size of the content
			    # transmitted *less* than the content-length!
			    f = open(path, 'rb')
			except IOError:
			    self.send_error(404, "File not found")
			    return None
			self.send_response(200)
			self.send_header("Content-type", ctype)
			self.send_header("Access-Control-Allow-Origin", "*")
			fs = os.fstat(f.fileno())
			self.send_header("Content-Length", str(fs[6]))
			self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
			self.end_headers()
			return f
	def do_GET(self):
		"""Serve a GET request."""
		f = self.send_head()
		if f:
			self.copyfile(f, self.wfile)
			f.close()
#class ThreadedHTTPServer(ThreadingMixIn, server):
#    """Handle requests in a separate thread."""
server_address = ("", 8000)
getHandler.cgi_directories = ["/cgi-bin"]
httpd = server(server_address,getHandler)
#srvobj = ThreadedHTTPServer(server_address, handler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile="./localhost.pem", server_side=True)
# Force the use of a subprocess, rather than
# normal fork behavior since that doesn't work with ssl
handler.have_fork=False
httpd.serve_forever()
