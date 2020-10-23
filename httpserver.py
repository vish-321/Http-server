#!/usr/bin/python
from socket import *
import sys
from threading import Thread
from Requests import Process_GET_Request
from status_codes import status_501,status_503

client_count=0;

def ProcessClient(connectionSocket):
	global client_count
	client_count+=1
	
	message=connectionSocket.recv(10240).decode()
	print(message)
	
		
	
	ProcessRequest(connectionSocket , message )
	
	return 
	
def ProcessRequest(connectionSocket , message):

	request=message.split()
	global client_count
	if client_count >100:
		status_503( connectionSocket,request)		# Service unavailable due to overload
		
	if request[0]=="GET" :
		Process_GET_Request(connectionSocket , request )
	elif request[0]=="POST" :
		Process_POST_Request(connectionSocket , request )
	elif request[0]=="PUT" :
		Process_GET_Request(connectionSocket , request )
	elif request[0]=="DELETE" :
		Process_GET_Request(connectionSocket , request ) 
	elif request[0]=="HEAD" :
		Process_GET_Request(connectionSocket , request ) 
	else :
		status_501(connectionSocket)
	
	client_count-=1

		
		
		

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

