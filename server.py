#!/usr/bin/python
from socket import *
import sys
from threading import Thread

connectionlist =[]

#	As I have used infinite loops everywhere to use chatroom for unlimited time
#	port is not closing  even after stoping server sometimes
#	So in such cases use folowing command to close port
#	sudo kill $(sudo lsof -t -i:12002)



def printchat(connectionSocket):
	message="Welcome to  chatroom!"
	connectionSocket.send(message.encode()) 
	
	
	while(True):
		
		message=connectionSocket.recv(1024)
		sendMessage(message)
	
	
	
	
def sendMessage(message) :
	for connection in connectionlist:
		connection.send(message)
		
		
		
		

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(100) 


print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept() ;
	connectionlist.append(connectionSocket)
	th= Thread(target=printchat,args=(connectionSocket,))
	th.start()













