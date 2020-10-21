#!/usr/bin/python
from socket import *
import sys
from threading import Thread
from Requests import Process_GET_Request


def ProcessClient(connectionSocket):


	message=connectionSocket.recv(20240).decode()
	print(message)
	ProcessRequest(connectionSocket , message )
	
	return 
	
def ProcessRequest(connectionSocket , message):

	request=message.split()
	
	if request[0]=="GET" :
		Process_GET_Request(connectionSocket , request )
	if request[0]=="POST" :
		Process_POST_Request(connectionSocket , request )
	if request[0]=="PUT" :
		Process_GET_Request(connectionSocket , request )
	if request[0]=="DELETE" :
		Process_GET_Request(connectionSocket , request ) 
	
	

		
		
		

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(100) 


print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept() ;
	print("New request received from ip: ") ; print (addr[0]);
	print("On port No: ") ; print (addr[1]);
	print ("connection socket is "); print (connectionSocket) ;
	th= Thread(target=ProcessClient,args=(connectionSocket,))
	th.start()
	
	
	
	
	
	
		
	
	












#	As I have used infinite loops everywhere to use chatroom for unlimited time
#	port is not closing  even after stoping server sometimes
#	So in such cases use folowing command to close port
#	sudo kill $(sudo lsof -t -i:12002)

