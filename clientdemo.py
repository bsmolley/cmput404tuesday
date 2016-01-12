#!/usr/bin/env python

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("www.google.com", 80))

request = "GET / HTTP/1.0\n\n"

clientSocket.sendall(request)

done = False
while not done:
	part = clientSocket.recv(2048)
	if part:
		print part
	else:
		done = True