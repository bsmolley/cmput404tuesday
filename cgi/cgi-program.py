#!/usr/bin/env python

from __future__ import print_function
import sys, os, cgi

print("Blah", file=sys.stderr)

#print("Content-type: text/plain")
print("Content-type: text/html")
print("")
#print("Hello, this is the CGI script!")
#print("I am process %i" % os.getpid())
print("<HTML><BODY><FORM method='POST'><INPUT name='x'></FORM></BODY></HTML>")

#print(os.environ)
#print("")
form = cgi.FieldStorage()
print(form.getvalue('x'))