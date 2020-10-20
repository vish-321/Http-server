from socket import *
import sys
import os
import datetime
from extra_functions import * 

ROOT="test_website"

def  Process_GET_Request(connectionSocket , request ) :

	if  (request[0]=="GET"):
	
		
		print("request[1]= "+ request[1]+"\n")
		if request[1]=="/" :
			request[1]+="index.html"
		requested_path=  ROOT + request[1]
		print("requested path= "+requested_path+"\n")
		
		if os.path.exists(requested_path) :
		
			response ="HTTP/1.1 200 OK\n"
			curr_time = datetime.datetime.now()
			response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\n")
			response+="Server: Vishal-Server\n"
			content_size= os.path.getsize(requested_path)
			
			response+="Content-Length: "+str (content_size) + "\n"
		#	response+="Connection: "+find_value("Connection:", request)+"\n"
			content_type = GetContentType(request[1])
			response+="Content-Type: "+content_type+ "\n\n"
			
			f= open(requested_path)
			body=f.read()
			response+=body
			connectionSocket.send(response.encode())
			
			connectionSocket.close()
			
			
			
			
			
