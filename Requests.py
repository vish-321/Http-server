from socket import *
import sys
import os
import datetime
from extra_functions import * 
from status_codes import *

ROOT="test_website"

def  Process_GET_Request(connectionSocket , request ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		status_414(connectionSocket,request)		#URI too long
		
	elif request[1].find('?') !=-1:
		payload= request[1][request[1].find('?')+1 :]
		words= payload.split('&')
		
		if words[0]=="email=vishalbhatane123%40gmail.com" and words[1]=="pswd=1234" :
			requested_path="test_website/homework.html"
			status_200(requested_path , connectionSocket , request)
		else :
			status_403(connectionSocket , request)  #request forbidden
	
		
	elif os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			
			if GetKeyValue("If-Range:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				status_304(requested_path,connectionSocket ,request) #not modified
				
			elif GetKeyValue("If-None-Match:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				status_304(requested_path,connectionSocket ,request)	#not modified
			else :
				status_200(requested_path, connectionSocket ,request) #called status_200 method froms status_codes		
		elif request[2]=="HTTP/1.0" :
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		if requested_path == "test_website/temp.html" :
			status_302(connectionSocket,request)	# found but moved to another URI
			
		elif requested_path=="test_website/location.html" :
			status_301(connectionSocket,request)	#moved permanantly
		else  :
			status_404 (connectionSocket ,request)	 #Not found
			
			
			
			
			




def  Process_HEAD_Request(connectionSocket , request ) :

	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/':
		status_400(connectionSocket,request)
		
	elif len(request[1])>2048 :
		status_414(connectionSocket,request)		#URI too long
		
	elif request[1].find("?") !=-1:
		payload= request[1][request[1].find("?")+1 :]
		
		words= payload.split('&')
		
		
		if words[0]=="email=vishalbhatane123%40gmail.com" and words[1]=="pswd=1234" :
			requested_path="test_website/homework.html"
			status_200(requested_path , connectionSocket , request)
		else :
			
			status_403(connectionSocket , request)		# Acess Forbidden 
	
		
		
	elif os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			if GetKeyValue("If-Range:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				status_304(requested_path,connectionSocket ,request) #Not modified
				
			elif GetKeyValue("If-None-Match:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				status_304(requested_path,connectionSocket ,request) #Not modified	
			else :
				status_200(requested_path, connectionSocket ,request) #called status_200 method froms status_codes		
				
		elif request[2]=="HTTP/1.0" :
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		if requested_path == "test_website/temp.html" :
			status_302(connectionSocket,request)	# found but moved to another URI
			
		elif requested_path=="test_website/location.html" :
			status_301(connectionSocket,request)	#moved permanantly
		else  :
			status_404 (connectionSocket ,request)	 #not found
			
			
			
			
			
			
			
			
			
			
def  Process_POST_Request(connectionSocket , request ,message ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		status_414(connectionSocket,request)		#URI too long
		
	
		
	elif os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			write_in_log_file (message)
			status_200(requested_path, connectionSocket ,request) # ok		
		elif request[2]=="HTTP/1.0" :
			status_426(connectionSocket,request) 	#Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			status_505(connectionSocket,request) 	#Htpp version not supported
			
				
			
		else :
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		write_in_log_file (message)
		status_201( connectionSocket ,request)
			
			
			
						
			
def  Process_PUT_Request(connectionSocket , request ,message ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		status_414(connectionSocket,request)		#URI too long
		
	
		
	elif os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			
			write_in_log_file (message)
			status_204(connectionSocket ,request) #No Content	
		elif request[2]=="HTTP/1.0" :
			status_426(connectionSocket,request) 	#Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			status_505(connectionSocket,request) 	#Htpp version not supported
			
				
			
		else :
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		write_in_log_file (message)
		status_201( connectionSocket ,request)		#Created
			
						




def  Process_DELETE_Request(connectionSocket , request ,message ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		status_414(connectionSocket,request)		#URI too long
		
	
		
	elif os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			status_200(requested_path, connectionSocket ,request) # ok		
		elif request[2]=="HTTP/1.0" :
			status_426(connectionSocket,request) 	#Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			status_505(connectionSocket,request) 	#Htpp version not supported
			
				
			
		else :
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		status_202 (connectionSocket ,request)	 #Accepted
			
			
		


			
