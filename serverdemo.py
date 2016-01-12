#!/usr/bin/env python

import socket, os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen on local machine address
# 0.0.0.0 = any address on this computer
serverSocket.bind(("0.0.0.0", 4555))

serverSocket.listen(5)

while True:
	(incomingSocket, address) = serverSocket.accept()

	childPid = os.fork()
	if (childPid != 0):
		# we must be still in the socket accepting processes
		continue

	outgoingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	outgoingSocket.connect(("www.google.com", 80))

	# we must be in a client talking process
	done = False
	while not done:
		# fix cpu use with poll() or select()
		
		incomingSocket.setblocking(0)
		try:
			part = incomingSocket.recv(2048)
		except IOError, exception:
			if exception.errno == 11:
				part = None
			else:
				raise

		if part:
			outgoingSocket.sendall(part)

		###

		outgoingSocket.setblocking(0)
		try:
			part = outgoingSocket.recv(2048)
		except IOError, exception:
			if exception.errno == 11:
				part = None
			else:
				raise

		if part:
			incomingSocket.sendall(part)