from socket import *
import sys
import os
import datetime
from extra_functions import * 

ROOT="test_website"







def status_200 (requested_path, connectionSocket ,request):
	response ="HTTP/1.1 200 OK\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	last_modified = os.path.getmtime(requested_path)
	response += ("Last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\r\n")
	response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
	response += "Accept-Ranges: bytes\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
		
	if request[0]=="HEAD" or  request[0]=="POST"  or request[0]=="PUT":
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
			
	
		
	else:
		if request[0]== "DELETE" :
			requested_path="errors/delete.html"
		content_size= os.path.getsize(requested_path)
				
		response+="Content-Length: "+str (content_size) + "\r\n"
			
		content_type = GetContentType(request[1])
		response+="Content-Type: "+content_type+ "\r\n\r\n"
		print(response)
		response=response.encode()
			
		response+= GetBodyContent(requested_path, content_type) #GetBodyContent implemented in extra_functions
		connectionSocket.send(response)
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
			
			

def status_201 ( connectionSocket ,request):
	response ="HTTP/1.1 201 Created\r\n"
	response+="Location: log.txt\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
	response += "Accept-Ranges: bytes\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
	connectionSocket.send(response.encode())
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
			
			
def status_202 ( connectionSocket ,request):
	response ="HTTP/1.1 202 Accepted\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
	response += "Accept-Ranges: bytes\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
		
	connectionSocket.send(response.encode())
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
			
			


def status_204 ( connectionSocket ,request):
	response ="HTTP/1.1 204 No Content\r\n"
	response+="Location: log.txt\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
	response += "Accept-Ranges: bytes\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
		
	connectionSocket.send(response.encode())
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
			
			





def status_400 ( connectionSocket ,request):
	response ="HTTP/1.1 400 Bad Request\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	
	requested_path="errors/error_400.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
		
		
		
def status_404 ( connectionSocket ,request):
	response ="HTTP/1.1 404 Not Found\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
		
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) != "keep-alive":
			connectionSocket.close()
		return
	
	requested_path="errors/error_404.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
	
	
	
	
	
	
				





def status_403 ( connectionSocket ,request):
	response ="HTTP/1.1 403 Forbidden\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
		
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) != "keep-alive":
			connectionSocket.close()
		return
	
	requested_path="errors/error_403.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
			
		
		
		








def status_408 ( connectionSocket ,request):
	response ="HTTP/1.1 408 Request Timeout\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response+="Connection: close\r\n" #it is mandatory to close connection in case of time out
	
	requested_path="errors/error_408.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close() # it is mandatory to close connection in case of time out 
		
	









def status_411 ( connectionSocket ,request):
	response ="HTTP/1.1 411 Length Required\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) != "keep-alive":
			connectionSocket.close()
		return
	requested_path="errors/error_411.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
	







def status_413 ( connectionSocket ,request):
	response ="HTTP/1.1 413 Payload Too Large\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	requested_path="errors/error_413.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
	





def status_414 ( connectionSocket ,request):
	response ="HTTP/1.1 414 URI Too Long\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) != "keep-alive":
			connectionSocket.close()
		return
	requested_path="errors/error_414.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
	







def status_426 ( connectionSocket ,request ):
	response ="HTTP/1.1 426 Upgrade Required\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	response+="Upgrade: HTTP/1.1\r\n"	# need to upgrade to version 1.1

	response+="Connection: Upgrade\r\n" # connection need to be upgraded
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		
		connectionSocket.close()
		return
	
	requested_path="errors/error_426.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close()
		
	


def status_500 ( connectionSocket ,request):
	response ="HTTP/1.1 500 Internal Server Error\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	
	
			
	
	response+="Connection: close\r\n"
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		
		connectionSocket.close()
		return
	
	
	requested_path="errors/error_500.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close()
		
		






		


def status_501 ( connectionSocket ,request):
	response ="HTTP/1.1 501 Method Not Implemented\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	
	response+="Allow: GET,HEAD,POST,PUT,DELETE\r\n"
			
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	
	requested_path="errors/error_501.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
		




def status_502 ( connectionSocket ,request):
	response ="HTTP/1.1 502 Bad Gateway\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) != "keep-alive":
			connectionSocket.close()
		return
	
	requested_path="errors/error_502.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
		









def status_503 ( connectionSocket ,request):
	response ="HTTP/1.1 503 Service Unavailable\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response+="Connection: close\r\n"
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		
		connectionSocket.close()
		return
	
	requested_path="errors/error_503.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close()
		
		


def status_504 ( connectionSocket ,request):
	response ="HTTP/1.1 504 Gateway Timeout\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	response+="Connection: close\r\n"
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		
		connectionSocket.close()
		return
	
	requested_path="errors/error_504.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close()
		
		

		
		
		
def status_505 ( connectionSocket ,request):
	response ="HTTP/1.1 505 HTTP Version Not Supported\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	
	response+="Connection: close\r\n"
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		
		connectionSocket.close()
		return
	
	requested_path="errors/error_505.html"
	content_size= os.path.getsize(requested_path)
			
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	
	connectionSocket.close()
		
		

		
		



		
def status_301 ( connectionSocket ,request):
	response ="HTTP/1.1 301 Moved Permanently\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
		
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	response+="location: /backend/location.html\r\n"
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
		return
	
	requested_path="errors/error_301.html"
	content_size= os.path.getsize(requested_path)
				
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
		
def status_302 ( connectionSocket ,request ):
	response ="HTTP/1.1 302 Found<\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
		
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
		
	response+="location: /backend/temp.html\r\n"
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
		return
		
	
	requested_path="errors/error_302.html"
	content_size= os.path.getsize(requested_path)
	
	response+="Content-Length: "+str (content_size) + "\r\n"
	response+="Content-Type: text/html; charset=iso-8859-1\r\n\r\n"
	
	print(response)
	response=response.encode()
			
	response+= GetBodyContent(requested_path, "text/html") #GetBodyContent implemented in extra_functions
	connectionSocket.send(response)
	if GetKeyValue("Connection:", request) == "close":
		connectionSocket.close()
		
		


def status_304 ( requested_path,connectionSocket ,request ):
	response ="HTTP/1.1 304 Not Modified\r\n"
	curr_time = datetime.datetime.now()
	response+= ("Date: " + curr_time.strftime("%A") + ", "+ curr_time.strftime("%d") + " " +  curr_time.strftime("%b") + " " + curr_time.strftime("%Y") + " " + curr_time.strftime("%X") + " GMT\r\n")
	response+="Server: Vishal-Server\r\n"
	
	
	last_modified = os.path.getmtime(requested_path)
	response += ("Last-Modified: " + datetime.datetime.fromtimestamp(last_modified).strftime("%A, %d %b, %Y %I:%M:%S")+ " GMT\r\n")
	response += 'ETag: "6d82cbb050ddc7fa9cbb659014546e59"\r\n'
	response += "Accept-Ranges: bytes\r\n"
				
	if GetKeyValue("Connection:", request) == "close":
		response+="Connection: close\r\n"
		
	else :
		response+="Connection: Keep-Alive\r\n"
		response+="Keep-Alive: timeout=5, max=1000\r\n"
	
	
	if request[0]=="HEAD" :
		connectionSocket.send(response.encode())
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
		
	else:
		content_size= os.path.getsize(requested_path)
				
		response+="Content-Length: "+str (content_size) + "\r\n"
			
		content_type = GetContentType(request[1])
		response+="Content-Type: "+content_type+ "\r\n\r\n"
		print(response)
		response=response.encode()
				
		response+= GetBodyContent(requested_path, content_type) #GetBodyContent implemented in extra_functions
		connectionSocket.send(response)
		if GetKeyValue("Connection:", request) == "close":
			connectionSocket.close()
			
			





		
	



		
