from socket import *
import sys
import os
import datetime
from extra_functions import * 

ROOT="test_website"

def  Process_GET_Request(connectionSocket , request ) :

	if  (request[0]=="GET"):
	
		
		
		if request[1]=="/" :
			request[1]+="index.html"
		requested_path=  ROOT + request[1]
		
		
		if os.path.exists(requested_path) :
		
			response ="HTTP/1.1 200 OK\r\n"
			curr_time = datetime.datetime.now()
			response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
			response+="Server: Vishal-Server\r\n"
			last_modified = os.path.getmtime(requested_path)
			response += ("Last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\r\n")
			response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
			response += "Accept-Ranges: bytes\r\n"
			
			if find_value("Connection:", request) != "keep-alive":
				response+="Connection: Keep-Alive\r\n"
				response+="Keep-Alive: timeout=5, max=1000\r\n"
			else :
				response+="Connection: close\r\n"
			content_size= os.path.getsize(requested_path)
			
			response+="Content-Length: "+str (content_size) + "\r\n"
		
			content_type = GetContentType(request[1])
			response+="Content-Type: "+content_type+ "\r\n\r\n"
			print(response)
			response=response.encode()
			
			response+= GetBodyContent(requested_path, content_type) #GetBodyContent implemented in extra_functions
			connectionSocket.send(response)
			if find_value("Connection:", request) != "keep-alive":
				connectionSocket.close()
			
			
			
			
			
			
			
			
