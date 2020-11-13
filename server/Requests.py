from socket import *
import sys
import os
import datetime
from extra_functions import * 
from status_codes import *

ROOT="../var/www/html"

def  Process_GET_Request(connectionSocket ,message, request,ip ,time) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		log=time
		log+=" "
		log+="[alert] "		# logging level for error_log
		log+="badly formatted request\n"
		write_log(log ,"error_log")
		
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="URI too long\n"
		write_log(log ,"error_log")
		status_414(connectionSocket,request)		#URI too long
		
	elif request[1].find('?') !=-1:
		payload= request[1][request[1].find('?')+1 :]
		words= payload.split('&')
		
		if words[0]=="email=vishalbhatane123%40gmail.com" and words[1]=="pswd=1234" :
			requested_path=ROOT+"/homework.html"
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]		#extra \n get added so to pop up that last character
			log+='"'
			log+=" 200"
			
			status_200(requested_path , connectionSocket , request,log)
		else :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="Invalid attempt to log in\n"
			write_log(log ,"error_log")
			status_403(connectionSocket , request)  #request forbidden
	
	requested_path=  ROOT + request[1]	
	if os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			
			if GetKeyValue("If-Range:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				
				log+=" 304"
				status_304(requested_path,connectionSocket ,request,log) #not modified
				
			elif GetKeyValue("If-None-Match:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				
				log+=" 304"
				status_304(requested_path,connectionSocket ,request,log)	#not modified
			else :
				
				log+=" 200"
				status_200(requested_path, connectionSocket ,request,log) #called status_200 method froms status_codes		
		elif request[2]=="HTTP/1.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from HTTP/1.0\n"
			write_log(log ,"error_log")
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from newer version than HTTP.1.1\n"
			write_log(log ,"error_log")
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			log=time
			log+=" "
			log+="[alert] "		# logging level for error_log
			log+="Badly formatted request\n"
			write_log(log ,"error_log")
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		if requested_path == ROOT+"/temp.html" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 302"
			
			status_302(connectionSocket,request,log)	# found but moved to another URI
			
		elif requested_path==ROOT+"/location.html" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 301"
			status_301(connectionSocket,request,log)	#moved permanantly
		else  :
			log=time
			log+=" "
			log+="[error] "		# logging level for error_log
			log+="Requested page Not found\n"
			write_log(log ,"error_log")
			status_404 (connectionSocket ,request)	 #Not found
			
			
			
			
			




def  Process_HEAD_Request(connectionSocket , request ,message ,ip ,time ) :

	if request[1]=="/" :
		request[1]+="index.html"
	requested_path=  ROOT + request[1]
	if  request[1][0]!='/' :
		log=time
		log+=" "
		log+="[alert] "		# logging level for error_log
		log+="badly formatted request\n"
		write_log(log ,"error_log")
		
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="URI too long\n"
		write_log(log ,"error_log")
		status_414(connectionSocket,request)		#URI too long
		
	elif request[1].find('?') !=-1:
		payload= request[1][request[1].find('?')+1 :]
		words= payload.split('&')
		
		if words[0]=="email=vishalbhatane123%40gmail.com" and words[1]=="pswd=1234" :
			requested_path=ROOT+"/homework.html"
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]		#extra \n get added so to pop up that last character
			log+='"'
			log+=" 200"
			
			status_200(requested_path , connectionSocket , request,log)
		else :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="Invalid attempt to log in\n"
			write_log(log ,"error_log")
			status_403(connectionSocket , request)  #request forbidden
	
	requested_path=  ROOT + request[1]	
	if os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			
			if GetKeyValue("If-Range:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				
				log+=" 304"
				status_304(requested_path,connectionSocket ,request,log) #not modified
				
			elif GetKeyValue("If-None-Match:", request)=='"6d82cbb050ddc7fa9cbb659014546e59"':
				
				log+=" 304"
				status_304(requested_path,connectionSocket ,request,log)	#not modified
			else :
				
				log+=" 200"
				status_200(requested_path, connectionSocket ,request,log) #called status_200 method froms status_codes		
		elif request[2]=="HTTP/1.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from HTTP/1.0\n"
			write_log(log ,"error_log")
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from newer version than HTTP/1.1\n"
			write_log(log ,"error_log")
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			log=time
			log+=" "
			log+="[alert] "		# logging level for error_log
			log+="badly formatted request\n"
			write_log(log ,"error_log")
			status_400(connectionSocket,request)	#Bad request
				
				
	else :
		
		if requested_path == ROOT+"/temp.html" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 302"
			
			status_302(connectionSocket,request,log)	# found but moved to another URI
			
		elif requested_path==ROOT+"/location.html" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 301"
			status_301(connectionSocket,request,log)	#moved permanantly
		else  :
			log=time
			log+=" "
			log+="[error] "		# logging level for error_log
			log+="Requested page Not found\n"
			write_log(log ,"error_log")
			status_404 (connectionSocket ,request)	 #Not found
			
			
			
			
			
	
			
			
			
			
			
			
			
def  Process_POST_Request(connectionSocket , request ,message ,ip ,time ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	
	if  request[1][0]!='/' :
		log=time
		log+=" "
		log+="[alert] "		# logging level for error_log
		log+="badly formatted request\n"
		write_log(log ,"error_log")
		
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="URI too long\n"
		write_log(log ,"error_log")
		status_414(connectionSocket,request)		#URI too long
		
		
	requested_path=  ROOT + request[1]	
	if os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			log=ip
			log+=" - - "   		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 200"
			write_in_log_file (message)	# This is just post content which is being written in dummy file
			status_200(requested_path, connectionSocket ,request,log) # ok		
		elif request[2]=="HTTP/1.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from HTTP/1.0\n"
			write_log(log ,"error_log")
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from newer version than HTTP/1.1\n"
			write_log(log ,"error_log")
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			log=time
			log+=" "
			log+="[alert] "		# logging level for error_log
			log+="badly formatted request\n"
			write_log(log ,"error_log")
			status_400(connectionSocket,request)	#Bad request
						
			
				
				
	else :
		log=ip
		log+=" - - "   		#logging format is %h %l %u %t %r %s %b
		log+=time
		log+=" "
		log+='"'
		log+=message.split('\n')[0]		# logging level for error_log
		log=log[:-1]
		log+='"'
		log+=" 201"
		write_in_log_file (message)		#write_in_log and write_log are different
		status_201( connectionSocket ,request,log)	#created
			
			
			
						
			
def  Process_PUT_Request(connectionSocket , request ,message ,ip ,time ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	
	if  request[1][0]!='/' :
		log=time
		log+=" "
		log+="[alert] "		# logging level for error_log
		log+="badly formatted request\n"
		write_log(log ,"error_log")
		
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="URI too long\n"
		write_log(log ,"error_log")
		status_414(connectionSocket,request)		#URI too long
		
		
	requested_path=  ROOT + request[1]
	if os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			log=ip
			log+=" - - "		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 204"
			write_in_log_file (message)	#This is just post content which is being written in dummy file
			status_204(requested_path, connectionSocket ,request,log) # No Content	
		elif request[2]=="HTTP/1.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from HTTP/1.0\n"
			write_log(log ,"error_log")
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from newer version than HTTP/1.1\n"
			write_log(log ,"error_log")
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			log=time
			log+=" "
			log+="[alert] "		# logging level for error_log
			log+="badly formatted request\n"
			write_log(log ,"error_log")
			status_400(connectionSocket,request)	#Bad request
						
	else :
		
		log=ip
		log+=" - - "   		#logging format is %h %l %u %t %r %s %b
		log+=time
		log+=" "
		log+='"'
		log+=message.split('\n')[0]		# logging level for error_log
		log=log[:-1]
		log+='"'
		log+=" 201"
		write_in_log_file (message)		#write_in_log and write_log are different
		status_201( connectionSocket ,request,log)	#created
			
				
						




def  Process_DELETE_Request(connectionSocket , request ,message ,ip ,time ) :
	
	if request[1]=="/" :
		request[1]+="index.html"
	
	if  request[1][0]!='/' :
		log=time
		log+=" "
		log+="[alert] "		# logging level for error_log
		log+="badly formatted request\n"
		write_log(log ,"error_log")
		
		status_400(connectionSocket,request)		#Bad Request 
		
	elif len(request[1])>2048 :
		log=time
		log+=" "
		log+="[error] "		# logging level for error_log
		log+="URI too long\n"
		write_log(log ,"error_log")
		status_414(connectionSocket,request)		#URI too long
		
		
	requested_path=  ROOT + request[1]
	if os.path.exists(requested_path) :
		if request[2]=="HTTP/1.1" :
			log=ip
			log+=" - - "		#logging format is %h %l %u %t %r %s %b
			log+=time
			log+=" "
			log+='"'
			log+=message.split('\n')[0]		# logging level for error_log
			log=log[:-1]
			log+='"'
			log+=" 204"
			write_in_log_file (message)	#This is just post content which is being written in dummy file
			status_204(requested_path, connectionSocket ,request,log) # No Content	
		elif request[2]=="HTTP/1.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from HTTP/1.0\n"
			write_log(log ,"error_log")
			status_426(connectionSocket,request) 	# Upgrade  required
				
		elif request[2]=="HTTP/2.0" or request[2]=="HTTP/3.0" :
			log=time
			log+=" "
			log+="[warn] "		# logging level for error_log
			log+="request from newer version than HTTP/1.1\n"
			write_log(log ,"error_log")
			status_505(connectionSocket,request) 	# Htpp version not supported
			
				
			
		else :
			log=time
			log+=" "
			log+="[alert] "		# logging level for error_log
			log+="badly formatted request\n"
			write_log(log ,"error_log")
			status_400(connectionSocket,request)	#Bad request
						
	else :
		
		log=ip
		log+=" - - "   		#logging format is %h %l %u %t %r %s %b
		log+=time
		log+=" "
		log+='"'
		log+=message.split('\n')[0]		# logging level for error_log
		log=log[:-1]
		log+='"'
		log+=" 202"
		status_202 (connectionSocket ,request,log)	 #Accepted
			
			
		


			
