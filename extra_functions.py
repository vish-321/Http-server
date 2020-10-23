from socket import *
import sys
import os
import datetime

def GetKeyValue(x, y):
    #x is the attribute of which value is to be found
    #y is the array in which the value to be found
    t = False
    for val in y:
        if t :
            return val
        if val == x:
            t = True
        return None


def GetBodyContent(requested_path, content_type):     
	if(content_type=="text/html") :
		f= open(requested_path)
		body=f.read()
		body=body.encode() 
		return body 
				
	else  :
		f=open(requested_path, 'rb')
		body=f.read()
		return body




def GetContentType(file_name):
    
    arr = file_name.split(".")
    if arr[1] == "html" or arr[1] == "htm" :
        return "text/html"
    elif arr[1] == "jpg" or arr[1] == "jpeg" or arr[1] == "png" or arr[1] == "gif":
        return "image/" + arr[1]
    else :
        return "text/html"
