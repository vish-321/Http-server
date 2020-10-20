from socket import *
import sys
import os
import datetime


def GetContentType(file_name):
    
    arr = file_name.split(".")
    if arr[1] == "html" or arr[1] == "htm" :
        return "text/html"
    elif arr[1] == "jpg" or arr[1] == "jpeg" or arr[1] == "png" or arr[1] == "gif":
        return "image/" + arr[1]
    else :
        return "text/html"
