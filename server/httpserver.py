#!/usr/bin/python
from socket import *
import sys
from threading import Thread
from Requests import Process_GET_Request
from status_codes import status_501,status_503,status_400
import datetime
from extra_functions import write_log
client_count=0;

def ProcessClient(connectionSocket, ip):
	global client_count
	client_count+=1
	
	message=connectionSocket.recv(10240).decode()
	
	curr_time = datetime.datetime.now()
	time= ("[" + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT]")  #current time addes to log
	
	print(message)
	
		
	
	ProcessRequest(connectionSocket , message ,ip ,time)
	
	return 
	
def ProcessRequest(connectionSocket , message ,ip,time ):
	
	request=message.split()
	
	global client_count
	if client_count >100:
		status_503( connectionSocket,request)		# Service unavailable due to overload
		
	if request[0]=="GET" :
		Process_GET_Request(connectionSocket ,message, request,ip ,time)
	elif request[0]=="POST" :
		Process_POST_Request(connectionSocket , request ,message ,ip ,time)
	elif request[0]=="PUT" :
		Process_PUT_Request(connectionSocket , request ,message,ip,time )
	elif request[0]=="DELETE" :
		Process_DELETE_Request(connectionSocket , request ,message,ip ,time ) 
	elif request[0]=="HEAD" :
		Process_HEAD_Request(connectionSocket , request,message,ip ,time) 
	else :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="requested method not implemented\n"
		write_log(log ,"error_log")
		status_501(connectionSocket,request  )			# Method not implemented 
			
		
	
	client_count-=1			# passing ip of remote and time which is used for logging

		
		
		

serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(100) 


print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept() ;
	ip=addr[0]
	print("New request received from ip: ") ; print (ip) ;
	  	
	
	
	print("On port No: ") ; print (addr[1]);
	print ("connection socket is "); print (connectionSocket) ;
	th= Thread(target=ProcessClient,args=(connectionSocket,ip,))
	th.start()
	



#	As I have used infinite loops everywhere to use chatroom for unlimited time
#	port is not closing  even after stoping server sometimes
#	So in such cases use folowing command to close port
#	sudo kill $(sudo lsof -t -i:12002)

